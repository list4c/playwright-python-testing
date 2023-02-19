import re

import pytest
from playwright.sync_api import expect

from pages.page_objects.navbar import Navbar, NavbarMenuOptions


def test_navbar_correct_links(navbar: Navbar, pytestconfig: pytest.Config) -> None:
    base_url = pytestconfig.getini("base_url")
    menu_items = list(NavbarMenuOptions().get_all_texts())
    menu_links = {
        f"{base_url}/{menu_text.lower()}"
        for menu_text in menu_items
        if menu_text != "Careers"
    }
    menu_links.add("https://career.stxnext.com")

    navbar.load_and_accept_cookies()

    assert (
        navbar.header_links.all_inner_texts() == menu_items
    ), "Navbar items are in incorrect order or text is not matching"
    assert (
        navbar.get_navbar_links_formatted() == menu_links
    ), "Navbar links have unexpected value"


def test_navbar_link_highlighting(navbar: Navbar) -> None:
    tested_page = NavbarMenuOptions.BLOG
    tested_page_pattern = re.compile(tested_page.lower())
    expected_css = ("color", "rgb(51, 202, 192)")

    navbar.load_and_accept_cookies()
    navbar.go_to_link(tested_page)
    blog_link = navbar.get_link(tested_page)

    expect(blog_link).to_have_css(*expected_css)
    expect(navbar.page).to_have_url(tested_page_pattern)


def test_navbar_search(navbar: Navbar) -> None:
    search_query = "asdfg"
    expected_search_results = (
        f"Sorry. There were no results for “{search_query}”"
        f".Try rewording your query, or browse through our site."
    )

    navbar.load_and_accept_cookies()
    navbar.search_phrase(search_query)

    expect(navbar.search_results).to_contain_text(expected_search_results)
