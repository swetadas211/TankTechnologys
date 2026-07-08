import pytest

from pages.footerpage import footer
@pytest.mark.smoke

def test_web_development(page):
    f1 = footer(page)
    f1.web_development_click()

def test_ecommerce(page):
    f1 = footer(page)
    f1.ecommerce_click()

def test_ui_ux_design(page):
    f2 = footer(page)
    f2.ui_ux_design_click()

def test_app_development(page):
    f3 = footer(page)
    f3.app_development_click()

def test_additional_app_links(page):
    f4 = footer(page)
    f4.additional_app_links_click()

def test_graphics_designing(page):
    f5= footer(page)
    f5.graphics_designing_click()



