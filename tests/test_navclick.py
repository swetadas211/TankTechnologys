import pytest

from pages.navclickpage import navmenu

@pytest.mark.smoke

def test_navclick(page):
    m1 = navmenu(page)
    m1.nav_click()
