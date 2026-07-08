import pytest

from pages.technologypage import technology
@pytest.mark.smoke     

def test_tech_hover(page):
    t1=technology(page)
    t1.tech_hover()

def test_ecommerce(page):
    t2=technology(page)
    t2.ecommerce_click()

def test_mobileApp(page):
    t3=technology(page)
    t3.mobileApp_click()
