import pytest

from pages.headerpage import header
@pytest.mark.smoke

def test_hedaer(page):
    h = header(page)
    h.freeQutoe_fill()