import pytest

from pages.contactuspage import contact
@pytest.mark.smoke

def test_contacutus(page):
    c1 = contact(page)
    c1.fill_contact()