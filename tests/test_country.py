import pytest

from pages.country import country
@pytest.mark.smoke

def test_country(page):
    r1=country(page)
    r1.country_click()