"""A Python package for scraping Japanese stock information from various web sites."""

from __future__ import annotations

from .jpx import Jpx
from .kabuyoho import Kabuyoho

__version__ = "0.0.4-rc4-post1"

kabuyoho = Kabuyoho()
jpx = Jpx()
