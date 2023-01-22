import pytest
from playwright.sync_api import Page

from pages.blog import StxBlogPage
from pages.main import StxMainPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


@pytest.fixture
def stx_page(page: Page):
    return StxMainPage(page)


@pytest.fixture
def blog_page(page: Page):
    return StxBlogPage(page)
