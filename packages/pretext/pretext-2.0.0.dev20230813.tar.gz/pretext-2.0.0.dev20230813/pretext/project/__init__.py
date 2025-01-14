import subprocess
import typing as t
from enum import Enum
import hashlib
import logging
import multiprocessing
import shutil
import tempfile
import pickle
from pathlib import Path
from lxml import etree as ET
from pydantic import validator, HttpUrl, PrivateAttr
import pydantic_xml as pxml
from .xml import Executables, LegacyProject, LatexEngine
from .. import constants
from .. import core
from .. import codechat
from .. import utils
from .. import types as pt  # PreTeXt types
from .. import templates


log = logging.getLogger("ptxlogger")

# TODO Not yet used...
# def optstrpth_to_posix(path: t.Optional[t.Union[Path, str]]) -> t.Optional[str]:
#     if path is None:
#         return None
#     else:
#         return Path(path).as_posix()


class Format(str, Enum):
    HTML = "html"
    LATEX = "latex"
    PDF = "pdf"
    EPUB = "epub"
    KINDLE = "kindle"
    BRAILLE = "braille"
    WEBWORK = "webwork"
    CUSTOM = "custom"


# The CLI only needs two values from the publication file. Therefore, this class ignores the vast majority of a publication file's contents, loading and validating only a (small) relevant subset.
class PublicationSubset(pxml.BaseXmlModel, tag="publication", search_mode="unordered"):
    external: Path = pxml.wrapped("source/directories", pxml.attr())
    generated: Path = pxml.wrapped("source/directories", pxml.attr())


class BrailleMode(str, Enum):
    EMBOSS = "emboss"
    ELECTRONIC = "electronic"


class Compression(str, Enum):
    ZIP = "zip"


# This class defines the possibilities of the `Target.platform`` attribute.
class Platform(str, Enum):
    # A typical HTML build, meant for self-hosting with no server configuration, features, or assumptions.
    WEB = "web"
    # Build output meant for hosting on a Runestone server.
    RUNESTONE = "runestone"


# Author can specify a method for asymptote generation.
class AsyMethod(str, Enum):
    LOCAL = "local"
    SERVER = "server"


# See `Target.server`.
class ServerName(str, Enum):
    SAGE = "sage"
    # Short for Asymptote.
    ASY = "asy"
    # Possible servers to add: Jing, WeBWorK.


# Allow the author to specify a server instead of a local executable for asset generation. See `Target.server`.
class Server(pxml.BaseXmlModel, tag="server"):
    name: ServerName = pxml.attr()
    url: HttpUrl = pxml.attr()


class Target(pxml.BaseXmlModel, tag="target", search_mode="unordered"):
    """
    Representation of a target for a PreTeXt project: a specific
    build targeting a format such as HTML, LaTeX, etc.
    """

    # Provide access to the containing project.
    _project: "Project" = PrivateAttr()
    # These two attribute are required; everything else is optional.
    name: str = pxml.attr()
    format: Format = pxml.attr()
    # These attributes have simple validators.
    #
    # A path to the root source for this target, relative to the project's `source` path.
    source: Path = pxml.attr(default=Path("main.ptx"))
    # A path to the publication file for this target, relative to the project's `publication` path. This is mostly validated by `post_validate`.
    publication: Path = pxml.attr(default=None)
    latex_engine: LatexEngine = pxml.attr(
        name="latex-engine", default=LatexEngine.XELATEX
    )
    braille_mode: BrailleMode = pxml.attr(
        name="braille-mode", default=BrailleMode.EMBOSS
    )
    stringparams: t.Dict[str, str] = pxml.element(default={})
    # A path to the subdirectory of your GitHub page where a book will be deployed for this target, relative to the project's `site` path.
    site: Path = pxml.attr(default=Path("site"))

    # These attributes have complex validators.
    #
    # The platform; only valid for an HTML target. See `Platform`. Define this before the other complex validators, since several depend on this value being set.
    platform: t.Optional[Platform] = pxml.attr()

    @validator(
        "platform",
        # Always run this, so we can provide a non-optional value for an HTML target.
        always=True,
    )
    def platform_validator(
        cls, v: t.Optional[Platform], values: t.Any
    ) -> t.Optional[Platform]:
        if values["format"] == Format.HTML:
            # For the HTML format, default to the web platform.
            if v is None:
                return Platform.WEB
        else:
            if v is not None:
                raise ValueError(
                    "Only the HTML format supports the platform attribute."
                )
        return v

    # We validate compression before output_filename to use its value to check if we can have an output_filename.
    compression: t.Optional[Compression] = pxml.attr()

    # Compression is only supported for HTML and WeBWorK formats.
    @validator("compression")
    def compression_validator(
        cls, v: t.Optional[Compression], values: t.Any
    ) -> t.Optional[Compression]:
        if values["format"] not in (Format.HTML, Format.WEBWORK) and v is not None:
            raise ValueError("Only the HTML and WeBWorK formats support compression.")
        if values["format"] == Format.HTML and values["platform"] == Platform.RUNESTONE:
            raise ValueError(
                "The HTML format for the Runestone platform does not allow compression."
            )
        return v

    # A path to the output directory for this target, relative to the project's `output` path.
    output_dir: Path = pxml.attr(name="output-dir", default=None)

    # Make the default value for output be `self.name`. Specifying a `default_factory` won't work, since it's a `@classmethod`. So, use a validator (which has access to the object), replacing `None` with `self.name`.
    @validator("output_dir", always=True)
    def output_dir_validator(cls, v: t.Optional[Path], values: t.Any) -> Path:
        # When the format is Runestone, this is overwritten in `post_validate`. Make sure it's not specified.
        if (
            values["format"] == Format.HTML
            and values["platform"] == Platform.RUNESTONE
            and v is not None
        ):
            raise ValueError("The Runestone format's output-dir must not be specified.")
        return Path(v) if v is not None else Path(values["name"])

    # A path to the output filename for this target, relative to the `output_dir`. The HTML target cannot specify this (since the HTML output is a directory of files, not a single file.)
    output_filename: t.Optional[str] = pxml.attr(name="output-filename", default=None)

    @validator("output_filename", always=True)
    def output_filename_validator(
        cls, v: t.Optional[str], values: t.Any
    ) -> t.Optional[str]:
        # See if `output-filename` is allowed.
        if (
            # WeBWorK always produces multiple files, so `output-filename` makes no sense.
            values["format"] == Format.WEBWORK
            or (
                # For the HTML format, non-zipped or Runestone output produces multiple files.
                values["format"] == Format.HTML
                and (
                    values["platform"] == Platform.RUNESTONE
                    or values["compression"] is None
                )
            )
            and v is not None
        ):
            raise ValueError(
                "The output_filename must not be present when the format is uncompressed HTML, Runestone, or Webwork."
            )
        # Verify that this is just a file name, without any prefixed path.
        assert v is None or Path(v).name == v
        return v

    # The method for generating asymptote files. Overrides the project's `asy_method` if specified.
    asy_method: t.Optional[AsyMethod] = pxml.attr(name="asy-method")

    # See `Server`. Each server name (`sage`, `asy`) may be specified only once. If specified, the CLI will use the server for asset generation instead of a local executable, unless @asy-method is set to "local". Settings for a given server name here override settings at the project level.
    server: t.List[Server] = pxml.element(default=[])

    @validator("server")
    def server_validator(cls, v: t.List[Server]) -> t.List[Server]:
        # Ensure the names are unique.
        if len(set([server.name for server in v])) != len(v):
            raise ValueError("Server names must not be repeated.")
        return v

    # A path to custom XSL for this target, relative to the project's `xsl` path.
    xsl: t.Optional[Path] = pxml.attr(default=None)

    # If the `format == Format.CUSTOM`, then `xsl` must be defined.
    @validator("xsl")
    def xsl_validator(cls, v: t.Optional[Path], values: t.Any) -> t.Optional[Path]:
        if v is None and values["format"] == Format.CUSTOM:
            raise ValueError("A custom format requires a value for xsl.")
        return v

    # Allow specifying `_project` in the constructor. (Since it's private, pydantic ignores it by default).
    def __init__(self, **kwargs: t.Any):
        super().__init__(**kwargs)
        if "_project" in kwargs:
            self._project = kwargs["_project"]
            # Since we now have the project, perform validation.
            self.post_validate()

    # Perform validation which requires the parent `Project` object. This can't be placed in a Pydantic validator, since `self._project` isn't set until after validation finishes. So, this must be manually called after that's done.
    def post_validate(self) -> None:
        # If no publication file is specified, assume either `publication.ptx` (if it exists) or the CLI's template `publication.ptx` (which always exists). If a publication file is specified, ensure that it exists.
        #
        # Select a default publication file if it's not provided.
        if self.publication is None:
            self.publication = Path("publication.ptx")
            # If this publication file doesn't exist, ...
            if not self.publication_abspath().exists():
                # ... then use the CLI's built-in template file.
                # TODO: this is wrong, since the returned path is only valid inside the context manager. Instead, need to enter the context here, then exit it when this class is deleted (also problematic).
                with templates.resource_path("publication.ptx") as self.publication:
                    pass
        # Otherwise, verify that the provided publication file exists. TODO: perhaps skip this, instead reporting a file open error when this is read?
        else:
            p_full = self.publication_abspath()
            if not p_full.exists():
                raise FileNotFoundError(
                    f"Provided publication file {p_full} does not exist."
                )
        # Pass `Project.asy_method` to `Target.asy_method` if it's not specified.
        self.asy_method = self.asy_method or self._project.asy_method

        # Merge `Project.server` with `self.server`; entries in `self.server` take precedence.
        self_server_names = [server.name for server in self.server]
        for server in self._project.server:
            if server.name not in self_server_names:
                self.server.append(server)

        # For the Runestone format, determine the `<document-id>`, which specifies the `output_dir`.
        if self.format == Format.HTML and self.platform == Platform.RUNESTONE:
            # We expect `d_list ==  ["document-id contents here"]`.
            d_list = self.source_element().xpath("/pretext/docinfo/document-id/text()")
            if isinstance(d_list, list):
                if len(d_list) != 1:
                    raise ValueError(
                        "Only one <document-id> is allowed in a PreTeXt document."
                    )
                d = d_list[0]
                assert isinstance(d, str)
                # Use the correct number of `../` to undo the project's `output-dir`, so the output from the build is located in the correct directory of `published/document-id`.
                self.output_dir = Path(
                    f"{'../'*len(self._project.output_dir.parents)}published/{d}"
                )
            else:
                raise ValueError(
                    "The <document-id> must be defined for the Runestone format."
                )

    def source_abspath(self) -> Path:
        return self._project.source_abspath() / self.source

    def source_element(self) -> ET._Element:
        source_doc = ET.parse(self.source_abspath())
        for _ in range(25):
            source_doc.xinclude()
        return source_doc.getroot()

    def publication_abspath(self) -> Path:
        return self._project.publication_abspath() / self.publication

    def output_dir_abspath(self) -> Path:
        return self._project.output_dir_abspath() / self.output_dir

    def xsl_abspath(self) -> t.Optional[Path]:
        if self.xsl is None:
            return None
        return self._project.xsl_abspath() / self.xsl

    def _read_publication_file_subset(self) -> PublicationSubset:
        p_bytes = self.publication_abspath().read_bytes()
        return PublicationSubset.from_xml(p_bytes)

    def external_dir(self) -> Path:
        return self._read_publication_file_subset().external

    def external_dir_abspath(self) -> Path:
        return (self.source_abspath().parent / self.external_dir()).resolve()

    def generated_dir(self) -> Path:
        return self._read_publication_file_subset().generated

    def generated_dir_abspath(self) -> Path:
        return (self.source_abspath().parent / self.generated_dir()).resolve()

    def ensure_asset_directories(self, asset: t.Optional[str] = None) -> None:
        self.external_dir_abspath().mkdir(parents=True, exist_ok=True)
        self.generated_dir_abspath().mkdir(parents=True, exist_ok=True)
        if asset is not None:
            # make directories for each asset type that would be generated from "asset":
            for asset_dir in constants.ASSET_TO_DIR[asset]:
                (self.generated_dir_abspath() / asset_dir).mkdir(
                    parents=True, exist_ok=True
                )

    def ensure_output_directory(self) -> None:
        log.debug(
            f"Ensuring output directory for {self.name}: {self.output_dir_abspath()}"
        )
        self.output_dir_abspath().mkdir(parents=True, exist_ok=True)

    def load_asset_table(self) -> pt.AssetTable:
        """
        Loads the asset table from a pickle file in the generated assets directory
        based on the target name.
        """
        try:
            with open(
                self.generated_dir_abspath() / f".{self.name}_assets.pkl", "rb"
            ) as f:
                return pickle.load(f)
        except Exception:
            return {}

    def generate_asset_table(self) -> pt.AssetTable:
        asset_hash_dict: pt.AssetTable = {}
        for asset in constants.ASSET_TO_XPATH.keys():
            if asset == "webwork":
                # WeBWorK must be regenerated every time *any* of the ww exercises change.
                ww = self.source_element().xpath(".//webwork[@*|*]")
                assert isinstance(ww, t.List)
                if len(ww) == 0:
                    # Only generate a hash if there are actually ww exercises in the source
                    continue
                asset_hash_dict[asset] = {}
                h = hashlib.sha256()
                for node in ww:
                    assert isinstance(node, ET._Element)
                    h.update(ET.tostring(node).strip())
                asset_hash_dict["webwork"][""] = h.digest()
            else:
                # everything else can be updated individually.
                # get all the nodes for the asset attribute
                source_assets = self.source_element().xpath(
                    constants.ASSET_TO_XPATH[asset]
                )
                assert isinstance(source_assets, t.List)
                if len(source_assets) == 0:
                    # Only generate a hash if there are actually assets of this type in the source
                    continue

                # We will have a dictionary of id's that we will get their own hash:
                asset_hash_dict[asset] = {}
                hash_ids = {}
                for node in source_assets:
                    assert isinstance(node, ET._Element)
                    # assign the xml:id of the youngest ancestor of the node with an xml:id as the node's id (or "" if none)
                    ancestor_xmlids = node.xpath("ancestor::*/@xml:id")
                    assert isinstance(ancestor_xmlids, t.List)
                    id = str(ancestor_xmlids[-1]) if len(ancestor_xmlids) > 0 else ""
                    assert isinstance(id, str)
                    # create a new hash object when id is first encountered
                    if id not in hash_ids:
                        hash_ids[id] = hashlib.sha256()
                    # update the hash with the node's xml:
                    hash_ids[id].update(ET.tostring(node).strip())
                    # and update the value of the hash for that asset/id pair
                    asset_hash_dict[asset][id] = hash_ids[id].digest()
        return asset_hash_dict

    def save_asset_table(self, asset_table: pt.AssetTable) -> None:
        """
        Saves the asset_table to a pickle file in the generated assets directory
        based on the target name.
        """
        with open(self.generated_dir_abspath() / f".{self.name}_assets.pkl", "wb") as f:
            pickle.dump(asset_table, f)

    def ensure_webwork_reps(self) -> None:
        """
        Ensures that the webwork representation file is present if the source contains webwork problems.  This is needed to build or generate other assets.
        """
        if self.source_element().xpath(".//webwork[@*|*]"):
            log.debug("Source contains webwork problems")
            if not (
                self.generated_dir_abspath() / "webwork" / "webwork-representations.xml"
            ).exists():
                log.debug("Webwork representations file does not exist, generating")
                self.generate_assets(
                    specified_asset_types=["webwork"], only_changed=False
                )
            else:
                log.debug("Webwork representations file exists, not generating")
        else:
            log.debug("Source does not contain webwork problems")

    def ensure_play_button(self) -> None:
        try:
            core.play_button(dest_dir=(self.generated_dir_abspath() / "play-button"))
            log.debug("Play button generated")
        except Exception as e:
            log.warning(f"Failed to generate play button: {e}")

    def clean_output(self) -> None:
        # refuse to clean if output is not a subdirectory of the project or contains source/publication
        if self._project.abspath() not in self.output_dir_abspath().parents:
            log.warning(
                "Refusing to clean output directory that isn't a proper subdirectory of the project."
            )
        # handle request to clean directory that does not exist
        elif not self.output_dir_abspath().exists():
            log.warning(
                f"Directory {self.output_dir_abspath()} already does not exist, nothing to clean."
            )
        # destroy the output directory
        else:
            log.warning(
                f"Destroying directory {self.output_dir_abspath()} to clean previously built files."
            )
            shutil.rmtree(self.output_dir_abspath())

    def build(
        self,
        clean: bool = False,
        no_generate: bool = False,
        xmlid: t.Optional[str] = None,
    ) -> None:
        # Check for xml syntax errors and quit if xml invalid:
        if not utils.xml_syntax_is_valid(self.source_abspath()):
            raise RuntimeError("XML syntax for source file is invalid")
        if not utils.xml_syntax_is_valid(self.publication_abspath(), "publication"):
            raise RuntimeError("XML syntax for publication file is invalid")
        # Validate xml against schema; continue with warning if invalid:
        utils.xml_source_validates_against_schema(self.source_abspath())

        # Clean output upon request
        if clean:
            self.clean_output()

        # Ensure the asset directories exist.
        self.ensure_asset_directories()

        # verify that a webwork_representations.xml file exists if it is needed; generated if needed.
        self.ensure_webwork_reps()

        # Generate needed assets unless requested not to.
        if not no_generate:
            self.generate_assets(xmlid=xmlid)

        # Ensure the output directories exist.
        self.ensure_output_directory()

        # Proceed with the build
        with tempfile.TemporaryDirectory() as tmp_xsl_str:
            tmp_xsl_path = Path(tmp_xsl_str)
            # if custom xsl, copy it into a temporary directory (different from the building temporary directory)
            if (txp := self.xsl_abspath()) is not None:
                log.info(f"Building with custom xsl {txp}")
                utils.copy_custom_xsl(txp, tmp_xsl_path)
                custom_xsl = tmp_xsl_path / txp.name
            else:
                custom_xsl = None

            # warn if "publisher" is one of the string-param keys:
            if "publisher" in self.stringparams:
                log.warning(
                    "You specified a publication file via a stringparam. "
                    + "This is ignored in favor of the publication file given by the "
                    + "<publication> element in the project manifest."
                )

            log.info(f"Preparing to build into {self.output_dir_abspath()}.")
            # The core expects `out_file` to be the full path, not just a file name, if it's not None.
            out_file = (
                (self.output_dir_abspath() / self.output_filename).as_posix()
                if self.output_filename is not None
                else None
            )
            if self.format == Format.HTML:
                # The copy allows us to modify these for the Runestone format below without affecting the original.
                sp = self.stringparams.copy()
                if self.platform == Platform.RUNESTONE:
                    # The validator guarantees this.
                    assert self.compression is None
                    assert self.output_filename is None
                    # This is equivalent to setting `<platform host="runestone">` in the publication file.
                    sp.update({"host-platform": "runestone"})
                core.html(
                    xml=self.source_abspath(),
                    pub_file=self.publication_abspath().as_posix(),
                    stringparams=sp,
                    xmlid_root=xmlid,
                    file_format=self.compression or "html",
                    extra_xsl=custom_xsl,
                    out_file=out_file,
                    dest_dir=self.output_dir_abspath().as_posix(),
                )
                codechat.map_path_to_xml_id(
                    self.source_abspath(),
                    self._project.abspath(),
                    self.output_dir_abspath().as_posix(),
                )
            elif self.format == Format.PDF:
                core.pdf(
                    xml=self.source_abspath(),
                    pub_file=self.publication_abspath().as_posix(),
                    stringparams=self.stringparams,
                    extra_xsl=custom_xsl,
                    out_file=out_file,
                    dest_dir=self.output_dir_abspath().as_posix(),
                    method=self.latex_engine,
                )
            elif self.format == Format.LATEX:
                core.latex(
                    xml=self.source_abspath(),
                    pub_file=self.publication_abspath().as_posix(),
                    stringparams=self.stringparams,
                    extra_xsl=custom_xsl,
                    out_file=out_file,
                    dest_dir=self.output_dir_abspath().as_posix(),
                )
            elif self.format == Format.EPUB:
                utils.npm_install()
                core.epub(
                    xml_source=self.source_abspath(),
                    pub_file=self.publication_abspath().as_posix(),
                    out_file=out_file,
                    dest_dir=self.output_dir_abspath().as_posix(),
                    math_format="svg",
                    stringparams=self.stringparams,
                )
            elif self.format == Format.KINDLE:
                utils.npm_install()
                core.epub(
                    xml_source=self.source_abspath(),
                    pub_file=self.publication_abspath().as_posix(),
                    out_file=out_file,
                    dest_dir=self.output_dir_abspath().as_posix(),
                    math_format="kindle",
                    stringparams=self.stringparams,
                )
            elif self.format == Format.BRAILLE:
                log.warning(
                    "Braille output is still experimental, and requires additional libraries from liblouis (specifically the file2brl software)."
                )
                utils.npm_install()
                core.braille(
                    xml_source=self.source_abspath(),
                    pub_file=self.publication_abspath().as_posix(),
                    out_file=out_file,
                    dest_dir=self.output_dir_abspath().as_posix(),
                    page_format=self.braille_mode,
                    stringparams=self.stringparams,
                )
            elif self.format == Format.WEBWORK:
                core.webwork_sets(
                    xml_source=self.source_abspath(),
                    pub_file=self.publication_abspath().as_posix(),
                    stringparams=self.stringparams,
                    dest_dir=self.output_dir_abspath().as_posix(),
                    tgz=self.compression,
                )
            elif self.format == Format.CUSTOM:
                # Need to add the publication file to string params since xsltproc function doesn't include pubfile.
                self.stringparams["publisher"] = self.publication_abspath().as_posix()
                core.xsltproc(
                    xsl=custom_xsl,
                    xml=self.source_abspath(),
                    result=out_file,
                    output_dir=self.output_dir_abspath().as_posix(),
                    stringparams=self.stringparams,
                )
            else:
                log.critical(f"Unknown format {self.format}")

    def generate_assets(
        self,
        specified_asset_types: t.Optional[t.List[str]] = None,
        all_formats: bool = False,
        only_changed: bool = True,
        xmlid: t.Optional[str] = None,
    ) -> None:
        if specified_asset_types is None or "ALL" in specified_asset_types:
            specified_asset_types = list(constants.ASSET_TO_XPATH.keys())
        log.debug(f"Assets generation requested for: {specified_asset_types}.")
        # We always build the asset hash table, even if only_changed=False: this tells us which assets need to be built, and how to update the saved asset hash table.
        source_asset_table = self.generate_asset_table()
        saved_asset_table = utils.clean_asset_table(
            self.load_asset_table(), source_asset_table
        )

        # Now we repeatedly pass through the source asset table, and purge any assets that we shouldn't build for any reason.
        # Throw away any asset types that were not requested:
        source_asset_table = {
            asset: source_asset_table[asset]
            for asset in source_asset_table
            if asset in specified_asset_types
        }
        # If we limit by xml:id, only look for assets below that id in the source tree
        if xmlid is not None:
            log.debug(f"Limiting asset generation to assets below xml:id={xmlid}.")
            # Keep webwork if only there is a webwork below the xmlid:
            ww_nodes = self.source_element().xpath(f"//*[@xml:id='{xmlid}']//webwork")
            assert isinstance(ww_nodes, t.List)
            if len(ww_nodes) == 0:
                source_asset_table.pop("webwork", None)
            # All other assets: we only need to keep the assets whose id is not above the xmlid (we would have used the xmlid as their id if there wasn't any other xmlid below it):
            # Get list of xml:ids below 'xmlid':
            id_list = self.source_element().xpath(f"//*[@xml:id='{xmlid}']//@xml:id")
            assert isinstance(id_list, t.List)
            # Filter by non-webwork assets whose id is in ID list:
            # Note: if an id = "", that means that no ancestor of that asset had an id, which means that it would not be a child of the xml:id we are subsetting.
            for asset in source_asset_table:
                if asset != "webwork":
                    source_asset_table[asset] = {
                        id: source_asset_table[asset][id]
                        for id in source_asset_table[asset]
                        if id in id_list
                    }
            log.debug(f"Eligible assets are: {source_asset_table.keys()}")

        # TODO: check which assets can be generated based on the user's system (and executables).

        # Now further limit the assets to be built by those that have changed since the last build, if only_changed is true.  Either way create a dictionary of asset: [ids] to be built, where asset:[] means to generate all of them.
        if only_changed:
            log.debug(
                "Checking whether any assets of changed and need to be regenerated."
            )
            for asset in source_asset_table:
                # Keep only the changed assets:
                source_asset_table[asset] = {
                    id: source_asset_table[asset][id]
                    for id in source_asset_table[asset]
                    if saved_asset_table.get(asset, {}).get(id, None)
                    != source_asset_table[asset][id]
                }
            log.debug(f"Assets to be regenerated: {source_asset_table.keys()}")
            # TODO: check if there are too many individual assets to make generating individually is worthwhile.
            assets_to_generate = {
                asset: [id for id in source_asset_table[asset]]
                for asset in source_asset_table
                if len(source_asset_table[asset]) > 0
            }
        else:
            assets_to_generate = {
                asset: [""]
                for asset in source_asset_table
                if (asset == "webwork" or len(source_asset_table[asset]) > 0)
            }

        # Finally, if we removed all assets from an asset type, remove that asset type:
        source_asset_table = {
            asset: source_asset_table[asset]
            for asset in source_asset_table
            if len(source_asset_table[asset]) > 0
        }

        # Now we have the correct list of assets we want to build.
        # We proceed to generate the assets that were requested.
        for asset in source_asset_table:
            self.ensure_asset_directories(asset)

        # Check if all formats are requested and modify accordingly.
        asset_formats = constants.ASSET_FORMATS[self.format]
        if all_formats:
            for asset in assets_to_generate:
                asset_formats[asset] = ["all"]

        # We will keep track of the assets that were successful to update cache at the end.
        successful_assets = []
        # generate assets by calling appropriate core functions :
        if "webwork" in assets_to_generate:
            try:
                core.webwork_to_xml(
                    xml_source=self.source_abspath(),
                    pub_file=self.publication_abspath().as_posix(),
                    stringparams=self.stringparams.copy(),
                    xmlid_root=xmlid,
                    abort_early=True,
                    dest_dir=(self.generated_dir_abspath() / "webwork").as_posix(),
                    server_params=None,
                )
                successful_assets.append(("webwork", ""))
            except Exception as e:
                log.debug(f"Unable to generate webwork: {e}")
        if "latex-image" in assets_to_generate:
            for id in assets_to_generate["latex-image"]:
                try:
                    for outformat in asset_formats["latex-image"]:
                        core.latex_image_conversion(
                            xml_source=self.source_abspath(),
                            pub_file=self.publication_abspath().as_posix(),
                            stringparams=self.stringparams.copy(),
                            xmlid_root=id,
                            dest_dir=self.generated_dir_abspath() / "latex-image",
                            outformat=outformat,
                            method=self.latex_engine,
                        )
                    successful_assets.append(("latex-image", id))
                except Exception as e:
                    log.debug(f"Unable to generate some latex-image assets: {e}")
        if "asymptote" in assets_to_generate:
            for id in assets_to_generate["asymptote"]:
                try:
                    for outformat in asset_formats["asymptote"]:
                        core.asymptote_conversion(
                            xml_source=self.source_abspath(),
                            pub_file=self.publication_abspath().as_posix(),
                            stringparams=self.stringparams.copy(),
                            xmlid_root=id,
                            dest_dir=self.generated_dir_abspath() / "asymptote",
                            outformat=outformat,
                            method=self.asy_method,
                        )
                    successful_assets.append(("asymptote", id))
                except Exception as e:
                    log.debug(f"Unable to generate some asymptote elements: {e}")

        if "sageplot" in assets_to_generate:
            for id in assets_to_generate["sageplot"]:
                try:
                    for outformat in asset_formats["sageplot"]:
                        core.sage_conversion(
                            xml_source=self.source_abspath(),
                            pub_file=self.publication_abspath().as_posix(),
                            stringparams=self.stringparams.copy(),
                            xmlid_root=id,
                            dest_dir=self.generated_dir_abspath() / "sageplot",
                            outformat=outformat,
                        )
                    successful_assets.append(("sageplot", id))
                except Exception as e:
                    log.debug(f"Unable to generate some sageplot images: {e}")

        if "interactive" in assets_to_generate:
            # Ensure playwright is installed:
            utils.playwright_install()
            for id in assets_to_generate["interactive"]:
                try:
                    core.preview_images(
                        xml_source=self.source_abspath(),
                        pub_file=self.publication_abspath().as_posix(),
                        stringparams=self.stringparams.copy(),
                        xmlid_root=id,
                        dest_dir=self.generated_dir_abspath() / "preview",
                    )
                    successful_assets.append(("interactive", id))
                except Exception as e:
                    log.debug(f"Unable to generate some interactive previews: {e}")
        if "youtube" in assets_to_generate:
            for id in assets_to_generate["youtube"]:
                try:
                    core.youtube_thumbnail(
                        xml_source=self.source_abspath(),
                        pub_file=self.publication_abspath().as_posix(),
                        stringparams=self.stringparams.copy(),
                        xmlid_root=id,
                        dest_dir=self.generated_dir_abspath() / "youtube",
                    )
                    successful_assets.append(("youtube", id))
                except Exception as e:
                    log.debug(f"Unable to generate some youtube thumbnails: {e}")
            # youtube also requires the play button.
            self.ensure_play_button()
        if "codelens" in assets_to_generate:
            for id in assets_to_generate["codelens"]:
                try:
                    core.tracer(
                        xml_source=self.source_abspath(),
                        pub_file=self.publication_abspath().as_posix(),
                        stringparams=self.stringparams.copy(),
                        xmlid_root=id,
                        dest_dir=self.generated_dir_abspath() / "trace",
                    )
                    successful_assets.append(("codelens", id))
                except Exception as e:
                    log.debug(f"Unable to generate some codelens traces: {e}")
        if "datafile" in assets_to_generate:
            for id in assets_to_generate["datafile"]:
                try:
                    core.datafiles_to_xml(
                        xml_source=self.source_abspath(),
                        pub_file=self.publication_abspath().as_posix(),
                        stringparams=self.stringparams.copy(),
                        xmlid_root=id,
                        dest_dir=self.generated_dir_abspath() / "datafile",
                    )
                    successful_assets.append(("datafile", id))
                except Exception as e:
                    log.debug(f"Unable to generate some datafiles: {e}")
        # Finally, also generate the qrcodes for interactive and youtube assets:
        # NOTE: we do not currently check for success of this for saving assets to the asset cache.
        if "interactive" in assets_to_generate or "youtube" in assets_to_generate:
            for id in set(
                assets_to_generate.get("interactive", [])
                + assets_to_generate.get("youtube", [])
            ):
                try:
                    core.qrcode(
                        xml_source=self.source_abspath(),
                        pub_file=self.publication_abspath().as_posix(),
                        stringparams=self.stringparams.copy(),
                        xmlid_root=id,
                        dest_dir=self.generated_dir_abspath() / "qrcode",
                    )
                except Exception as e:
                    log.debug(f"Unable to generate some qrcodes: {e}", exc_info=True)

        # Delete temporary directories left behind by core:
        core.release_temporary_directories()
        # After all assets are generated, update the asset cache:
        log.debug(f"Updated these assets successfully: {successful_assets}")
        for asset_type, id in successful_assets:
            assert isinstance(id, str)
            if asset_type not in saved_asset_table:
                saved_asset_table[asset_type] = {}
            if id == "":
                # We have updated all assets of this type, so update all of them in the saved asset table:
                for id in source_asset_table[asset_type]:
                    saved_asset_table[asset_type][id] = source_asset_table[asset_type][
                        id
                    ]
            else:
                if id in source_asset_table[asset_type]:
                    saved_asset_table[asset_type][id] = source_asset_table[asset_type][
                        id
                    ]
        # Save the asset table to disk:
        self.save_asset_table(saved_asset_table)
        log.debug(f"Saved asset table to disk: {saved_asset_table}")


class Project(pxml.BaseXmlModel, tag="project", search_mode="unordered"):
    """
    Representation of a PreTeXt project: a Path for the project
    on the disk, and Paths for where to build output and maintain a site.

    To create a Project object from a project.ptx file, use the `Project.parse()` method.
    """

    ptx_version: t.Literal["2"] = pxml.attr(name="ptx-version")
    _executables: Executables = PrivateAttr(default=Executables())
    # A path, relative to the project directory (defined by `self.abspath()`), prepended to any target's `source`.
    source: Path = pxml.attr(default=Path("source"))
    # The absolute path of the project file (typically, `project.ptx`).
    _path: Path = PrivateAttr(default=Path("."))

    # Allow a relative path; if it's a directory, assume a `project.ptx` suffix. Make the path absolute.
    @classmethod
    def validate_path(cls, path: t.Union[Path, str]) -> Path:
        path = Path(path).resolve()
        # Note: we don't require the `project.ptx` file to exist, since this can be created from API calls instead of being read in from a project file.
        return path / "project.ptx" if path.is_dir() else path

    # A path, relative to the project directory, prepended to any target's `publication`.
    publication: Path = pxml.attr(default=Path("publication"))
    # A path, relative to the project directory, prepended to any target's `output_dir`.
    output_dir: Path = pxml.attr(name="output-dir", default=Path("output"))
    # A path prepended to any target's `site`.
    site: Path = pxml.attr(default=Path("site"))
    # A path, relative to the project directory, prepended to any target's `xsl`.
    xsl: Path = pxml.attr(default=Path("xsl"))
    targets: t.List[Target] = pxml.wrapped(
        "targets", pxml.element(tag="target", default=[])
    )

    # The method for generating asymptote images can be specified at the project level, and overridden at the target level.
    asy_method: t.Optional[AsyMethod] = pxml.attr(
        name="asy-method", default=AsyMethod.SERVER
    )

    # See the docs on `Target.server`; they apply here as well.
    server: t.List[Server] = pxml.element(default=[])

    @validator("server")
    def server_validator(cls, v: t.List[Server]) -> t.List[Server]:
        # Ensure the names are unique.
        if len(set([server.name for server in v])) != len(v):
            raise ValueError("Server names must not be repeated.")
        return v

    # Allow specifying `_path` or `_executables` in the constructor. (Since they're private, pydantic ignores them by default).
    def __init__(self, **kwargs: t.Any):
        super().__init__(**kwargs)
        for k in ("_path", "_executables"):
            if k in kwargs:
                setattr(self, k, kwargs[k])
        self._path = self.validate_path(self._path)
        # Always initialize core when a project is created:
        self.init_core()

    @classmethod
    def parse(
        cls,
        path: t.Union[Path, str] = Path("."),
    ) -> "Project":
        _path = cls.validate_path(path)
        # TODO: nicer errors if these files aren't found.
        xml_bytes = _path.read_bytes()

        # Determine the version of this project file.
        class ProjectVersionOnly(pxml.BaseXmlModel, tag="project"):
            ptx_version: t.Optional[str] = pxml.attr(name="ptx-version")

        p_version_only = ProjectVersionOnly.from_xml(xml_bytes)
        if p_version_only.ptx_version is not None:
            p = Project.from_xml(xml_bytes)

            # Now that the project is loaded, load / set up what isn't in the project XML.
            p._path = _path
            try:
                e_bytes = (p._path.parent / "executables.ptx").read_bytes()
            except FileNotFoundError:
                # If this isn't found, use the already-set default value.
                pass
            else:
                p._executables = Executables.from_xml(e_bytes)

        else:
            legacy_project = LegacyProject.from_xml(_path.read_bytes())
            # Legacy projects didn't specify a base output directory, so we need to move up one level.
            # Translate from old target format to new target format.
            new_targets: t.List[Target] = []
            for tgt in legacy_project.targets:
                compression: t.Optional[Compression] = None
                braille_mode: t.Optional[BrailleMode] = None
                if tgt.format == "html-zip":
                    format = Format.HTML
                    compression = Compression.ZIP
                elif tgt.format == "webwork-sets":
                    format = Format.WEBWORK
                elif tgt.format == "webwork-sets-zipped":
                    format = Format.WEBWORK
                    compression = Compression.ZIP
                elif tgt.format == "braille-electronic":
                    format = Format.BRAILLE
                    braille_mode = BrailleMode.ELECTRONIC
                elif tgt.format == "braille-emboss":
                    format = Format.BRAILLE
                    braille_mode = BrailleMode.EMBOSS
                else:
                    format = Format(tgt.format.value)
                d = tgt.dict()
                del d["format"]
                # Remove the `None` from optional values, so the new format can replace these.
                for key in ("site", "xsl", "latex_engine"):
                    if d[key] is None:
                        del d[key]
                # Include the braille mode only if it was specified.
                if braille_mode is not None:
                    d["braille_mode"] = braille_mode
                new_target = Target(
                    format=format,
                    compression=compression,
                    **d,
                )
                new_targets.append(new_target)

            # Incorrect from a type perspective, but used to translate from old to new classes.
            legacy_project.targets = new_targets  # type: ignore
            p = Project(
                ptx_version="2",
                _path=_path,
                # Rename from `executables` to `_executables` when moving from the old to new project format.
                _executables=legacy_project.executables,
                # Since there was no `publication` path in the old format, use an empty path. (A nice feature: if all target publication files begin with `publication`, avoid this.)
                publication=Path(""),
                # The same is true for these paths.
                source=Path(""),
                output_dir=Path(""),
                site=Path(""),
                xsl=Path(""),
                **legacy_project.dict(),
            )

        # Set the `_project` for each target, which isn't handled in the XML.
        for _tgt in p.targets:
            _tgt._project = p
            _tgt.post_validate()
        return p

    def new_target(self, name: str, format: str, **kwargs: t.Any) -> None:
        self.targets.append(
            Target(name=name, format=Format(format), _project=self, **kwargs)
        )

    def _get_target(
        self,
        # If `name` is `None`, return the default (first) target; otherwise, return the target given by `name`.
        name: t.Optional[str] = None
        # Returns the target if found, or `None`` if it's not found.
    ) -> t.Optional["Target"]:
        if len(self.targets) == 0:
            # no target to return
            return None
        if name is None:
            # return default target
            return self.targets[0]
        try:
            # return first target matching the provided name
            return next(t for t in self.targets if t.name == name)
        except StopIteration:
            # but no such target was found
            return None

    # Return `True` if the target exists.
    def has_target(
        self,
        # See `name` from `_get_target`.
        name: t.Optional[str] = None,
    ) -> bool:
        return self._get_target(name) is not None

    def get_target(
        self,
        # See `name` from `_get_target`.
        name: t.Optional[str] = None,
    ) -> "Target":
        t = self._get_target(name)
        assert t is not None
        if name is None:
            log.info(f'Since no target was supplied, we will use "{t.name}".\n')
        return t

    def target_names(self, *args: str) -> t.List[str]:
        # Optional arguments are formats: returns list of targets that have that format.
        names = []
        for target in self.targets:
            if not args or target.format in args:
                names.append(target.name)
        return names

    def abspath(self) -> Path:
        # Since `_path` stores the path to the project file, the parent of this gives the directory it resides in.
        return self._path.parent

    def source_abspath(self) -> Path:
        return self.abspath() / self.source

    def publication_abspath(self) -> Path:
        return self.abspath() / self.publication

    def output_dir_abspath(self) -> Path:
        return self.abspath() / self.output_dir

    def site_abspath(self) -> Path:
        return self.abspath() / self.site

    def xsl_abspath(self) -> Path:
        return self.abspath() / self.xsl

    def server_process(
        self,
        output_dir: Path,
        access: t.Literal["public", "private"] = "private",
        port: int = 8128,
        launch: bool = True,
    ) -> multiprocessing.Process:
        """
        Returns a process for running a simple local web server
        providing the contents of the output directory.
        """
        return multiprocessing.Process(
            target=utils.serve_forever,
            args=[self.abspath(), output_dir, access, port, not launch],
        )

    def get_executables(self) -> Executables:
        return self._executables

    def init_core(self) -> None:
        core.set_executables(self._executables.dict())

    def deploy_targets(self) -> t.List[Target]:
        return [target for target in self.targets if target.site is not None]

    def deploy(self, target_name: str, update_source: bool) -> None:
        # Before doing any work, we check that git is installed.
        try:
            subprocess.run(["git", "--version"], capture_output=True)
            log.debug("Git is installed.")
        except Exception as e:
            log.error(
                "Git must be installed to use this feature, but couldn't be found."
            )
            log.debug(f"Error: {e}", exc_info=True)
            return
        # Determine what set of targets to deploy.  If a target name is specified, deploy on that target.  If there are `deploy-dir` specified in the project manifest, also deploy the contents of the `site` folder, if present.
        if len(self.deploy_targets()) == 0:
            target = self.get_target(target_name)
            if target is None:
                log.error(f"Target `{target_name}` not found.")
                return
            if target.format != Format.HTML:  # redundant for CLI
                log.error("Only HTML targets are supported.")
                return
            if not target.output_dir_abspath().exists():
                log.error(
                    f"No build for `{target.name}` was found in the directory `{target.output_dir_abspath()}`."
                )
                log.error(
                    f"Try running `pretext view {target.name} -b` to build and preview your project first."
                )
                return
            log.info(f"Using latest build located in `{target.output_dir_abspath()}`.")
            log.info("")
            utils.publish_to_ghpages(target.output_dir_abspath(), update_source)
            return
        else:  # we now deploy multiple targets and the site directory
            if not self.site_abspath().exists():
                log.error(f"Site directory `{self.site}` not found.")
                log.info(
                    f"You have `deploy-dir` or `site` (v2) elements in your project.ptx file, which requires you to maintain at least a simple landing page in the folder `{self.site}`. Either create this folder or remove the `deploy-dir` elements from your project.ptx file.\n"
                )
                return
            with tempfile.TemporaryDirectory() as temp_dir:
                shutil.copytree(
                    self.site.resolve(),
                    Path(temp_dir),
                    dirs_exist_ok=True,
                )
                for target in self.deploy_targets():
                    if not target.output_dir_abspath().exists():
                        log.warning(
                            f"No build for `{target.name}` was found in the directory `{target.output_dir_abspath()}`. Try running `pretext build {target.name}` to build this component first."
                        )
                        log.info("Skipping this target for now.")
                    else:
                        deploy_dir = str(target.site)
                        assert isinstance(deploy_dir, str)
                        shutil.copytree(
                            target.output_dir_abspath(),
                            (Path(temp_dir) / deploy_dir).resolve(),
                            dirs_exist_ok=True,
                        )
                        log.info(f"Deploying `{target.name}` to `{target.site}`.")
                # Recopy the site's index.html (if it exists) to the root of the temp directory.  This is a bit of a hack, but it's the simplest way to ensure that the site's landing page is deployed.
                if (self.site_abspath() / "index.html").exists():
                    shutil.copy(
                        self.site_abspath() / "index.html",
                        Path(temp_dir),
                    )
                utils.publish_to_ghpages(Path(temp_dir), update_source)
        return
