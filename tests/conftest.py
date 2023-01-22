import pytest
from pages.main_page import STXMainPage
from pages.blog_page import STXBlogPage
from playwright.sync_api import Page

@pytest.fixture
def blog_page(page: Page) -> STXBlogPage:
    return STXBlogPage(page)

@pytest.fixture
def main_page(page: Page) -> STXMainPage:
    return STXMainPage(page)