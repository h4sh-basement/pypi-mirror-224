"""
Display character blots in the terminal.

This module contains the functionality for formatting demicode's character blots
on screen. Its high-level functions are:

  * `add_presentation()` turns a stream of Unicode code points into one of
    presentation and code point pairs; for supported code points it adds
    variation selectors and combining characters.
  * `format_lines()` and `format_grid_lines()` turn the stream of presentation,
    code point pairs into a stream of formatted lines.
  * `page_lines()` displays a stream of lines, one screen at a time, and handles
    the user interaction.

The line-level functions are `format_legend()`, `format_heading()`, and
`format_info()`. The legend goes on top of a screen and headings are embedded in
the body. `format_info()` handles one presentation, code point pair per
invocation, generating a background and a foreground character blot.
"""

from collections.abc import Iterator, Iterable
from enum import auto, Enum
import itertools
from typing import cast, Literal, overload

from .render import Padding, Renderer
from .codepoint import CodePoint
from .ucd import UCD


class Presentation(Enum):
    """The presentation style for displaying a character.

    `PLAIN` displays just a character. It is the only valid presentation for
    most Unicode code points. The other presentation styles add further code
    points:

      * `CORNER` adds U+FE00 variation selector-1
      * `CENTER` adds U+FE01 variation selector-2
      * `TEXT` adds U+FE0E variation selector-15
      * `EMOJI` adds U+FE0F variation selector-16
      * `KEYCAP` adds U+FE0F variation selector-16 and U+20E3 combining
        enclosing keycap

    `CORNER` and `CENTER` may be used with the full-width forms of `!,.:;?`
    (U+FF01, U+FF0C, U+FF0E, U+FF1A, U+FF1B, U+FF1F), `TEXT` and `EMOJI` with
    the code points included in `USD.with_emoji_variation`, and `KEYCAP` with
    `#*0123456789`, which also are in `USD.with_emoji_variation`.
    """

    PLAIN = auto()
    CORNER = auto()
    CENTER = auto()
    TEXT = auto()
    EMOJI = auto()
    KEYCAP = auto()

    @property
    def variation_selector(self) -> str:
        match self:
            case Presentation.PLAIN:
                return '   '
            case Presentation.CORNER:
                return ' 1 '
            case Presentation.CENTER:
                return ' 2 '
            case Presentation.TEXT:
                return '15 '
            case Presentation.EMOJI:
                return '16 '
            case Presentation.KEYCAP:
                return '16 '


# --------------------------------------------------------------------------------------


LEGEND = ' 123 123 Code Pt  Ct Wd VS  Age Name'
LEGEND_WIDTH = len(LEGEND)
MIN_NAME_LENGTH = 4


def _max_name_length(width: int) -> int:
    if width <= LEGEND_WIDTH:
        return MIN_NAME_LENGTH
    return width - LEGEND_WIDTH + MIN_NAME_LENGTH


def format_legend(renderer: Renderer) -> str:
    """Format the legend for lines formatted with `format_info`."""
    if not renderer.has_style:
        return LEGEND[4:]

    flexible_spaces = _max_name_length(renderer.width) - MIN_NAME_LENGTH
    return renderer.legend(LEGEND + (' ' * flexible_spaces))


def format_heading(renderer: Renderer, heading: str) -> str:
    """
    Format the given heading. The initial \\u0001 (Start of Heading) is
    discarded.
    """
    if heading[0] == '\u0001':
        heading = heading[1:]

    left = LEGEND_WIDTH - 5
    if not renderer.has_style:
        left -= 4
    right = renderer.width - LEGEND_WIDTH + MIN_NAME_LENGTH - len(heading) - 1
    return renderer.heading(f'{"─" * left} {heading} {"─" * right}')


def format_info(
    renderer: Renderer,
    codepoint: CodePoint,
    *,
    start_column: int = 1,
    include_char_info: bool = True,
    presentation: Presentation = Presentation.PLAIN,
) -> Iterator[str]:
    """
    Format the fixed-width information for the given code point.

    If `include_char_info` is `True`, this function emits one line per code
    point. After showing the codepoint against a lightly colored background and
    a darkly colored foreground, this function also displays:

      * the hexadecimal value of the code point,
      * the general category,
      * the East Asian Width,
      * whether it used text or emoji variation selectors,
      * the Unicode version that introduced the code point,
      * and the name followed by the block in parentheses.

    If `include_char_info` is `False`, this function only displays the
    character, assuming it is a visible and not, for example, a surrogate or
    unassigned code point.

    The brightness controls how colorful the output is. At the default of 0,
    both background and foreground are colored in greys. At 1, the background
    turns a bright yelllow and, at 2, the foreground turns a bright orange. That
    generally works for the one code point per line format, but I do not
    recommend cranking up the brightness for the grid format.
    """
    # What to show?
    name_prefix = None
    category = UCD.category(codepoint)
    wcwidth = UCD.fixed_width(codepoint)

    if category is None or category.is_invalid or wcwidth == -1:
        wcwidth = 1
        display = '\uFFFD' # REPLACEMENT CHARACTER
    elif UCD.is_line_break(codepoint):
        display = '\u23CE' # RETURN SYMBOL
    elif presentation is Presentation.CORNER:
        assert codepoint in UCD.fullwidth_punctuation
        display = f'{chr(codepoint)}\uFE00'
    elif presentation is Presentation.CENTER:
        assert codepoint in UCD.fullwidth_punctuation
        display = f'{chr(codepoint)}\uFE01'
    elif presentation is Presentation.TEXT:
        assert codepoint in UCD.with_emoji_variation
        display = f'{chr(codepoint)}\uFE0E'
    elif presentation is Presentation.EMOJI:
        assert codepoint in UCD.with_emoji_variation
        display = f'{chr(codepoint)}\uFE0F'
    elif presentation is Presentation.KEYCAP:
        assert codepoint in UCD.with_keycap
        display = f'{chr(codepoint)}\uFE0F\u20E3'
        name_prefix = 'KEYCAP '
    else:
        display = chr(codepoint)

    # Render against background and against foreground
    yield renderer.column(start_column + 1)
    yield renderer.blot(display, Padding.BACKGROUND, 3 - wcwidth)
    yield ' '
    yield renderer.column(start_column + 5)
    yield renderer.blot(display, Padding.FOREGROUND, 3 - wcwidth)
    yield ' '

    # More information about the codepoint
    if include_char_info:
        yield renderer.column(start_column + 9)
        yield f'{str(codepoint):<8s} '
        yield '-- ' if category is None else f'{category.value} '
        east_asian_width = UCD.east_asian_width(codepoint)
        yield '-- ' if east_asian_width is None else f'{east_asian_width.value:<2s} '
        yield presentation.variation_selector
        age = UCD.age(codepoint)
        yield ' --- ' if age is None else f'{age:>4s} '

        name = UCD.name(codepoint)
        if name is None:
            name = str(codepoint)
        block = UCD.block(codepoint)
        if block is not None:
            name = f'{name} ({block})'
        if name_prefix is not None:
            name = name_prefix + name
        max_length = _max_name_length(renderer.width)
        if len(name) > max_length:
            name = name[:max_length - 1] + '…'
        yield f'{name}'


# --------------------------------------------------------------------------------------


@overload
def add_presentation(
    data: Iterable[CodePoint|str], *, headings: Literal[False]
) -> Iterator[tuple[Presentation, CodePoint]]: ...

@overload
def add_presentation(
    data: Iterable[CodePoint|str], *, headings: bool = ...
) -> Iterator[tuple[Presentation, CodePoint]|tuple[str, None]]: ...

def add_presentation(
    data: Iterable[CodePoint|str],
    *,
    headings: bool = True,  # Allow embedded headings
) -> Iterator[tuple[Presentation, CodePoint]|tuple[str, None]]:
    """
    Enrich code points with their presentation. This function takes a stream of
    code points interspersed with headings and enriches each code point with its
    presentation. For most code points, that means just adding the `PLAIN`
    presentation. However, for some, that means repeating the code point with
    different presentation options. Headings are passed through the function,
    unless `headings` is `False`, in which case they are dropped.
    """
    for datum in data:
        if isinstance(datum, str):
            if headings:
                yield datum, None
            continue
        if datum in UCD.fullwidth_punctuation:
            yield Presentation.CORNER, datum
            yield Presentation.CENTER, datum
        elif datum in UCD.with_emoji_variation:
            yield Presentation.TEXT, datum
            yield Presentation.EMOJI, datum
            if datum in UCD.with_keycap:
                yield Presentation.KEYCAP, datum
        else:
            yield Presentation.PLAIN, datum


def format_lines(
    renderer: Renderer,
    data: Iterable[tuple[Presentation, CodePoint]|tuple[str, None]],
) -> Iterator[str]:
    """Emit the extended, per-line representation for all code points."""
    for presentation, codepoint in data:
        if isinstance(presentation, str):
            yield format_heading(renderer, presentation)
        else:
            yield ''.join(format_info(
                renderer,
                cast(CodePoint, codepoint),
                presentation=presentation,
            ))


def format_grid_lines(
    renderer: Renderer,
    codepoints: Iterable[tuple[Presentation, CodePoint]],
) -> Iterator[str]:
    """Emit the compact, grid-like representation for all code points."""
    column_count = (renderer.width - 1) // 11
    while True:
        line = ''.join(itertools.chain.from_iterable(
            format_info(
                renderer,
                codepoint,
                presentation=presentation,
                start_column=count * 11 + 2,
                include_char_info=False,
            )
            for count, (presentation, codepoint)
            in enumerate(itertools.islice(codepoints, column_count))
        ))
        if line == '':
            return
        yield line


def page_lines(
    renderer: Renderer,
    legend: None | str,
    lines: Iterable[str],
) -> None:
    """Display one page of lines at a time."""

    hint = renderer.hint(' <return>: next page; q<return>/ctrl-c: quit') + ' '
    legend_height = 0 if legend is None else len(legend.splitlines())

    while True:
        renderer.refresh()
        body_height = renderer.height - legend_height - 1
        body = [*itertools.islice(lines, body_height)]

        actual_body_height = len(body)
        if actual_body_height == 0:
            return
        if actual_body_height < body_height:
            body.extend([''] * (body_height - actual_body_height))

        page = '\n'.join(itertools.chain([] if legend is None else [legend], body))
        print(page)

        try:
            s = input(hint).lower()
        except KeyboardInterrupt:
            return
        if s == 'q' or s == 'quit':
            return
