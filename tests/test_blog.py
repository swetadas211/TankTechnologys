import pytest

from pages.blogpage import blog

@pytest.mark.smoke
def test_blog_hover(page):
    b1 = blog(page)
    b1.blog_hover()