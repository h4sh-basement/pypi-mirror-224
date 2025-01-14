from __future__ import annotations

import logging

from typing import Any

from mknodes import config, mknav
from mknodes.basenodes import mknode
from mknodes.pages import mkpage
from mknodes.utils import helpers


logger = logging.getLogger(__name__)


class MkLink(mknode.MkNode):
    """A simple Link."""

    ICON = "octicons/link-24"
    REQUIRED_EXTENSIONS = ["attr_list"]  # for buttons

    def __init__(
        self,
        target: str | mkpage.MkPage | mknav.MkNav,
        title: str | None = None,
        icon: str | None = None,
        as_button: bool = False,
        primary_color: bool = False,
        **kwargs: Any,
    ):
        """Constructor.

        Arguments:
            target: Link target
            title: Title used for link
            icon: Optional icon to be displayed in front of title
            as_button: Whether link should be rendered as button
            primary_color: If rendered as button, use primary color as background.
            kwargs: keyword arguments passed to parent
        """
        super().__init__(**kwargs)
        self.target = target
        self.title = title
        self.as_button = as_button
        self.primary_color = primary_color
        icon = icon or ""
        self.icon = icon

    def __repr__(self):
        return helpers.get_repr(
            self,
            target=self.target,
            title=self.title,
            icon=self.icon,
            as_button=self.as_button,
            primary_color=self.primary_color,
            _filter_empty=True,
            _filter_false=True,
        )

    def get_url(self) -> str:  # type: ignore[return]
        import mknodes

        site_url = config.get_site_url() or ""
        match self.target:
            case mknodes.MkPage():
                path = self.target.resolved_file_path.replace(".md", ".html")
                return site_url + path
            case mknodes.MkNav():
                if self.target.index_page:
                    path = self.target.index_page.resolved_file_path
                    path = path.replace(".md", ".html")
                else:
                    path = self.target.resolved_file_path
                return site_url + path
            case str() if self.target.startswith("/"):
                return site_url.rstrip("/") + self.target
            case str() if self.target.startswith(("http:", "https:", "www.")):
                return self.target
            case str():
                return f"{self.target}.md"
            case _:
                raise TypeError(self.target)

    def _to_markdown(self) -> str:
        url = self.get_url()
        title = self.target if self.title is None else self.title
        if self.as_button:
            button_suffix = (
                "{ .md-button .md-button--primary }"
                if self.primary_color
                else "{ .md-button }"
            )
        else:
            button_suffix = ""
        icon = (
            self.icon
            if not self.icon or self.icon.startswith(":")
            else f':{self.icon.replace("/", "-")}:'
        )
        prefix = f"{icon} " if self.icon else ""
        return f"[{prefix}{title}]({url}){button_suffix}"

    @staticmethod
    def create_example_page(page):
        import mknodes

        url = "http://www.google.de"
        node = mknodes.MkLink(url, "This is a link.")
        page += mknodes.MkReprRawRendered(node, header="### Regular")
        node = mknodes.MkLink(url, "Disguised as button.", as_button=True)
        page += mknodes.MkReprRawRendered(node, header="### Button")
        node = mknodes.MkLink(url, "Colored.", as_button=True, primary_color=True)
        page += mknodes.MkReprRawRendered(node, header="### Colored")
        node = mknodes.MkLink(url, "With icon.", icon="octicons/link-24")
        page += mknodes.MkReprRawRendered(node, header="### With icon")
        node = mknodes.MkLink(page.parent.index_page, "To page.")
        page += mknodes.MkReprRawRendered(node, header="###To page")


if __name__ == "__main__":
    link = MkLink("www.test.de")
