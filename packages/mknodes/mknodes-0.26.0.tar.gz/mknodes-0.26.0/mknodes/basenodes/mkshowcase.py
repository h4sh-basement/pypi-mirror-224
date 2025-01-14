from __future__ import annotations

from collections.abc import Generator, Iterable
import itertools
import logging
import textwrap

from typing import Any, TypeVar
from xml.etree import ElementTree

from mknodes import mknav
from mknodes.basenodes import mkcontainer, mknode
from mknodes.pages import mkpage
from mknodes.utils import helpers


logger = logging.getLogger(__name__)


def get_xml_string(*, link: str, image: str, title: str, size: int, caption: str):
    root = ElementTree.Element("a", href=link)
    card_div = ElementTree.SubElement(root, "div", {"class": "card"})
    container_div = ElementTree.SubElement(card_div, "div", {"class": "container"})
    ElementTree.SubElement(
        container_div,
        "img",
        src=image,
        alt=title,
        style=f"width:{size}px,height:{size}px",
    )
    overlay_div = ElementTree.SubElement(container_div, "div", {"class": "overlay"})
    overlay_div.text = caption
    p = ElementTree.SubElement(card_div, "p")
    button = ElementTree.SubElement(p, "button")
    button.text = title
    return ElementTree.tostring(root, encoding="unicode")


T = TypeVar("T")


def batched(iterable: Iterable[T], n: int) -> Generator[tuple[T, ...], None, None]:
    """Batch data into tuples of length n. The last batch may be shorter."""
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        msg = "n must be at least one"
        raise ValueError(msg)
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch


class MkShowcaseCard(mknode.MkNode):
    """A simple Link."""

    ICON = "material/square-medium"
    STATUS = "new"
    CSS = "css/grid.css"

    def __init__(
        self,
        title: str,
        image: str,
        caption: str,
        target: str | mkpage.MkPage | mknav.MkNav | None = None,
        size: int = 200,
        **kwargs: Any,
    ):
        """Constructor.

        Arguments:
            title: Button text
            image: Card image
            caption: Image caption
            target: Link target. Can be a URL, an MkPage, or an MkNav
            size: Height/Width of the card
            kwargs: keyword arguments passed to parent
        """
        super().__init__(**kwargs)
        self.target = target
        self.title = title
        self.image = image
        self.caption = caption
        self.size = size

    def __repr__(self):
        return helpers.get_repr(
            self,
            target=self.target,
            title=self.title,
            image=self.image,
            caption=self.caption,
        )

    @property
    def url(self) -> str:  # type: ignore[return]
        if self.associated_project:
            config = self.associated_project.config
            base_url = config.site_url or ""
        else:
            base_url = ""
        return helpers.get_url(self.target, base_url)

    def _to_markdown(self) -> str:
        return get_xml_string(
            link=self.url,
            title=self.title,
            caption=self.caption,
            size=200,
            image=self.image,
        )


class MkShowcase(mkcontainer.MkContainer):
    """Node for showing a html-based image grid.

    This node requires addtional CSS to work.
    """

    ICON = "material/view-grid"
    CSS = "css/grid.css"

    def __init__(
        self,
        cards: list[str | mknode.MkNode] | None = None,
        column_count: int = 3,
        *,
        header: str = "",
        **kwargs,
    ):
        match cards:
            case None:
                items = []
            case list():
                items = [self.to_item(card) for card in cards]
        self.column_count = column_count
        super().__init__(content=items, header=header, **kwargs)

    def __repr__(self):
        return helpers.get_repr(self, cards=self.items)

    def to_item(self, item) -> MkShowcaseCard:
        match item:
            case mkpage.MkPage():
                return MkShowcaseCard(
                    target=item,
                    title=item.title or " ",
                    caption=item.subtitle or " ",
                    image=":material-tab:",
                    parent=self,
                )
            case MkShowcaseCard():
                return item
            case _:
                raise TypeError(item)

    def _to_markdown(self) -> str:
        text = ""
        for items in batched(self.items, self.column_count):
            text += '<div class="row">'
            for item in items:
                text += '\n  <div class="column">'
                text += textwrap.indent(str(item), "    ")
                text += "\n  </div>"
            text += "\n</div>"
        return text

    def add_card(
        self,
        title: str,
        image: str,
        link: str | None = None,
        caption: str = "",
    ):
        card = MkShowcaseCard(target=link, title=title, image=image, caption=caption)
        self.append(card)

    @staticmethod
    def create_example_page(page):
        import mknodes

        node = MkShowcase()
        for i in range(9):
            node.add_card(
                link="https://phil65.github.io/mknodes/",
                title=f"Title {i}",
                image="https://picsum.photos/200",
                caption=f"Caption {i}",
            )
        page += mknodes.MkReprRawRendered(node)


if __name__ == "__main__":
    import mknodes

    keys = mknodes.MkKeys(keys="Ctrl+A")
    grid = MkShowcase()
    grid.add_card("Tse", "td", "http://www.google.com")
    print(grid.items[0])
