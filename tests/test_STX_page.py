import pytest
from playwright.sync_api import Page, expect
from pages.main_page import STXMainPage
from pages.blog_page import STXBlogPage


def test_open_blog_page(
        page: Page,
        main_page: STXMainPage,
        blog_page: STXBlogPage) -> None:

    # Given the STX main page is displayed
    main_page.load()

    # When the user clicks on Blog button
    main_page.blog_button.click()

    # Then the STX blog page is displayed
    expect(page).to_have_url(blog_page.URL)


def test_search_blog_articles(
        page: Page,
        blog_page: STXBlogPage) -> None:

    # Given the STX blog page is displayed
    blog_page.load()

    # And the cookie consent button is accepted

    page.get_by_role("button", name="Accept").click()

    # When the user searches for a phrase
    blog_page.search.click()
    blog_page.search.fill("Software Testing and Quality Assurance")
    blog_page.search.press("Enter")

    # Then a popup with search results is displayed
    expect(blog_page.main_popup).to_be_visible()

    # And the search results contain the phrase

    expect(page.get_by_role("heading", name="The Business Manager’s Guide to Software Testing and Quality Assurance")).to_be_visible()
