from html import escape, unescape

import random
import re

ws_pattern = re.compile(r'\s+', flags=re.UNICODE)


def zalgonate(text: str, rng: bool = True, range_low: int = 4, range_high: int = 50) -> str:
    if not rng:
        random.seed(text)
    zalgotext = ""
    for c in text:
        zalgotext += add_diacritics(c, range_low, range_high)
    return escape(zalgotext)


def add_diacritics(c: str, lo: int, hi: int) -> str:
    if ws_pattern.sub('', c):
        return c + ''.join([get_random_diacritic() for _ in range(random.randint(lo, hi))])
    return c


def get_random_diacritic() -> str:
    return chr(random.randint(768, 879))
