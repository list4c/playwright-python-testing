import pytest
from playwright.sync_api import Page

from pages.page_objects.blog_page import BlogPage
from pages.page_objects.main_page import MainPage
from pages.page_objects.navbar import Navbar


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1920,
            'height': 1080,
        },
    }


@pytest.fixture()
def navbar(page: Page):
    return Navbar(page)


@pytest.fixture()
def blog_page(page: Page):
    return BlogPage(page)


@pytest.fixture()
def main_page(page: Page):
    return MainPage(page)
