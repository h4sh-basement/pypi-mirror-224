"""
Demicode's command line tool.
"""

import argparse
from collections.abc import Iterable, Sequence
import itertools
from pathlib import Path
import re
from textwrap import dedent

from .codepoint import CodePoint
from .darkmode import is_darkmode
from .ucd import UCD
from .display import (
    add_presentation,
    format_grid_lines,
    format_legend,
    format_lines,
    page_lines,
)
from .render import Mode, Renderer, StyledRenderer
from demicode import __version__


HEX_CODEPOINT = re.compile(r'(U[+])?[0-9A-Fa-f]{4,6}')


def width_limited_formatter(prog: str) -> argparse.HelpFormatter:
    return argparse.RawTextHelpFormatter(prog, width=70)


def configure_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='demicode',
        description="""        "It's not just Unicode, it's hemi-semi-demicode!\"""",
        epilog=dedent("""
            Demicode's output is paged. Press <return> to advance to the next
            page. If you enter "q" or "quit" before the <return>, demicode
            terminates immediately. It does the same if you press <control-c>.

            Demicode requires a terminal emulator that supports Ansi escape
            codes including 256 colors. Demicode is © 2023 Robert Grimm,
            licensed as open source under Apache 2.0.

                      <https://github.com/apparebit/demicode>
        """),
        formatter_class=width_limited_formatter,
    )

    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

    ucd_group = parser.add_argument_group('configure UCD')
    ucd_group.add_argument(
        '--ucd-path',
        help='set path for local mirror of UCD',
    )
    ucd_group.add_argument(
        '--ucd-version',
        help='set UCD version from 4.1 onwards',
    )

    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

    cp_group = parser.add_argument_group('select code points')
    cp_group.add_argument(
        '--with-arrows',
        action='store_true',
        help='include codepoints for matching regular and long arrows',
    )
    cp_group.add_argument(
        '--with-dashes',
        action='store_true',
        help='include codepoints with Unicode\'s Dash property',
    )
    cp_group.add_argument(
        '--with-emoji-variation',
        action='store_true',
        help='include all codepoints that have text and\nemoji variations'
    )
    cp_group.add_argument(
        '--with-keycaps',
        action='store_true',
        help='include codepoints that combine with U+20E3\ninto enclosing keycaps'
    )
    cp_group.add_argument(
        '--with-lingchi',
        action='store_true',
        help='include several highlights for incoherent\nand inconsistent widths'
    )
    cp_group.add_argument(
        '--with-mad-dash',
        action='store_true',
        help ='include indistinguishable dashes'
    )
    cp_group.add_argument(
        '--with-version-oracle',
        action='store_true',
        help='include emoji that date supported Unicode version'
    )
    cp_group.add_argument(
        '--with-curation',
        action='store_true',
        help='include curated selection of codepoints'
    )
    cp_group.add_argument(
        'codepoints',
        nargs='*',
        help="""include codepoints provided as space-
separated hex numbers (4-6 digits, optionally
prefixed with "U+") or as literal characters
without intermediate spaces"""
    )

    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

    out_group = parser.add_argument_group('control output')
    out_group.add_argument(
        '--in-grid', '-g',
        action='store_true',
        help='display as grid without further UCD information'
    )
    out_group.add_argument(
        '--in-dark-mode', '-d',
        default=None,
        action='store_true',
        help='use colors suitable for dark mode'
    )
    out_group.add_argument(
        '--in-light-mode', '-l',
        action='store_false',
        dest='in_dark_mode',
        help='use colors suitable for light mode',
    )
    out_group.add_argument(
        '--in-more-color', '-c',
        default=0,
        action='count',
        help='use brighter colors in output;\nmay be repeated once'
    )
    out_group.add_argument(
        '--in-plain-text', '-p',
        action='store_true',
        help='display plain text without ANSI escape codes'
    )

    # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

    about_group = parser.add_argument_group('about this tool')
    about_group.add_argument(
        '--stats',
        action='store_true',
        help='display summary statistics and exit'
    )
    about_group.add_argument(
        '--version',
        action='store_true',
        help='display the package version and exit'
    )

    return parser


# --------------------------------------------------------------------------------------


def run(arguments: Sequence[str]) -> int:
    # -------------------------- Parse the options and prepare console renderer
    parser = configure_parser()
    options = parser.parse_args(arguments[1:])

    if options.in_dark_mode is None:
        options.in_dark_mode = is_darkmode()

    new_renderer = Renderer if options.in_plain_text else StyledRenderer
    renderer = new_renderer(
        Mode.DARK if options.in_dark_mode else Mode.LIGHT,
        options.in_more_color
    )

    # ---------------------------------------------- Set UCD path and/or version
    try:
        if options.ucd_path:
            UCD.use_path(Path(options.ucd_path))
        if options.ucd_version:
            UCD.use_version(options.ucd_version)
    except ValueError as x:
        print(renderer.error(f'Error: {str(x)}'))
        return 1

    # ------------------------------------------------ Handle version and stats
    if options.version:
        print(renderer.very_strong(f' demicode {__version__} '))
        return 0

    if options.stats:
        print()
        print(renderer.strong('Code Points with Given Property'))
        print()
        print(f'    dash            : {len(UCD.dashes):4,d}')
        print(f'    keycap          : {len(UCD.with_keycap):4,d}')
        print(f'    noncharacter    : {len(UCD.noncharacters):4,d}')
        print(f'    selector        : {len(UCD.selectors):4,d}')
        print(f'    emoji variation : {len(UCD.with_emoji_variation):4,d}')
        print(f'    white space     : {len(UCD.whitespace):4,d}')
        print()
        return 0

    # ---------------------------------------- Determine code points to display
    codepoints: list[Iterable[CodePoint|str]] = []
    if options.with_arrows:
        codepoints.append(UCD.arrows)
    if options.with_dashes:
        codepoints.append(sorted(UCD.dashes))
    if options.with_emoji_variation:
        codepoints.append(sorted(UCD.with_emoji_variation))
    if options.with_keycaps:
        codepoints.append(sorted(UCD.with_keycap))
    if options.with_lingchi:
        codepoints.append(UCD.lingchi)
    if options.with_mad_dash:
        codepoints.append(UCD.mad_dash)
    if options.with_version_oracle:
        codepoints.append(UCD.version_oracle)
    if options.with_curation:
        codepoints.append(UCD.mad_dash)
        codepoints.append(UCD.lingchi)
        codepoints.append(UCD.version_oracle)
    if options.codepoints:
        # Both hexadecimal numbers and characters are recognized.
        for argument in options.codepoints:
            if HEX_CODEPOINT.match(argument):
                codepoints.append([CodePoint.of(argument)])
            else:
                codepoints.append(CodePoint.of(ch) for ch in argument)

    # -------------------------------- If there's nothing to display, help user
    if len(codepoints) == 0:
        print(renderer.error('Error: There are no codepoints to show.'))
        print(renderer.error('Maybe try again with "1F49D" as argument——'))
        print(renderer.error('or with "-h" to see all options.'))
        return 1

    # ----------------------------------------------------- Display code points
    if options.in_grid:
        page_lines(
            renderer,
            None,
            format_grid_lines(
                renderer,
                add_presentation(
                    itertools.chain.from_iterable(codepoints),
                    headings=False
                ),
            ),
        )
    else:
        page_lines(
            renderer,
            format_legend(renderer),
            format_lines(
                renderer,
                add_presentation(itertools.chain.from_iterable(codepoints)),
            ),
        )

    # -------------------------------------------------------------------- Done
    return 0
