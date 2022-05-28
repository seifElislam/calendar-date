"""
Calendars module
"""
from .gregorian import Gregorian
from .hijri import Hijri
from .coptic import Coptic

order = [
    Gregorian,
    Hijri,
    Coptic
]
