import html

import random
import re

ws_pattern = re.compile(r'\s+', flags=re.UNICODE)


def zalgonate(text: str, rng: bool = True, range_low: int = 4, range_high: int = 50, bold: bool = False) -> str:
    if not rng:
        random.seed(text)

    zalgotext = ""

    for c in text:
        zalgotext += add_diacritics(c, range_low, range_high, bold)

    return html_escape(zalgotext)


def add_diacritics(c: str, lo: int, hi: int, bold: bool = False) -> str:
    if ws_pattern.sub('', c):
        if bold:
            c = boldify(c)
        return c + ''.join([get_random_diacritic() for _ in range(random.randint(lo, hi))])
    return c


def get_random_diacritic() -> str:
    return chr(random.randint(768, 879))


def html_escape(text: str):
    return html.escape(text).replace('\n', '<br/>')


def boldify(c: str) -> str:
    if 65 <= ord(c) <= 90:
        return chr(ord(c) + 0x1d3bf)
    if 97 <= ord(c) <= 122:
        return chr(ord(c) + 0x1d3b9)
    return c