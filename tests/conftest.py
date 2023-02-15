import pytest
from playwright.sync_api import Page

from pages.blog_page import StxBlogPage
from pages.main_page import StxMainPage


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
def blog_page(page: Page) -> StxBlogPage:
    return StxBlogPage(page)


@pytest.fixture
def main_page(page: Page) -> StxMainPage:
    return StxMainPage(page)
