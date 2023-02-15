import pytest
from playwright.sync_api import expect

from pages.page_objects.main_page import MainPage


def test_open_blog_page(main_page: MainPage, pytestconfig: pytest.Config) -> None:
    base_url = pytestconfig.getini("base_url")
    blog_url = f"{base_url}/blog"
    main_page.load()
    main_page.accept_cookies()

    expect(main_page.blog_btn).to_have_attribute("href", blog_url)
