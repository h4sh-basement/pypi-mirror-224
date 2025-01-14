from __future__ import annotations

import dataclasses

from typing import Literal


RAW_GITHUB = "https://raw.githubusercontent.com"

BuildSystemStr = Literal["hatch", "flit", "poetry", "setuptools", "pdm"]


@dataclasses.dataclass
class BuildSystem:
    identifier: BuildSystemStr
    build_backend: str
    url: str
    env_setup_cmd: str | None
    install_url: str | None = None


hatch = BuildSystem(
    identifier="hatch",
    build_backend="hatchling.build",
    url="https://hatch.pypa.io",
    env_setup_cmd="hatch env create",
    install_url=f"{RAW_GITHUB}/pypa/hatch/master/docs/install.md",
)
flit = BuildSystem(
    identifier="flit",
    build_backend="flit_core.buildapi",
    url="https://flit.pypa.io",
    env_setup_cmd="flit install",
)
poetry = BuildSystem(
    identifier="poetry",
    build_backend="poetry.core.masonry.api",
    url="https://python-poetry.org",
    env_setup_cmd="poetry install",
)
setuptools = BuildSystem(
    identifier="setuptools",
    build_backend="setuptools.build_meta",
    url="https://pypi.org/project/setuptools/",
    env_setup_cmd=None,
)
pdm = BuildSystem(
    identifier="pdm",
    build_backend="pdm.backend",
    url="https://pdm.fming.dev/",
    env_setup_cmd="pdm install",
    install_url=f"{RAW_GITHUB}/pdm-project/pdm/main/docs/docs/index.md#Installation",
)

BUILD_SYSTEMS: dict[BuildSystemStr, BuildSystem] = {
    p.identifier: p for p in [hatch, flit, poetry, setuptools, pdm]
}
