import pytest
from playwright.sync_api import Page, expect

from pages.blog_page import StxBlogPage
from pages.main_page import StxMainPage


def test_open_blog_page(
    page: Page, main_page: StxMainPage, blog_page: StxBlogPage
) -> None:

    # Given the STX main page is displayed
    main_page.load()

    # When the user clicks on Blog button
    main_page.blog_button.click()

    # Then the STX blog page is displayed
    expect(page).to_have_url(blog_page.URL)


def test_search_blog_articles(page: Page, blog_page: StxBlogPage) -> None:

    keyword = "test"
    article_title = (
        "The Business Manager’s Guide to Software Testing and Quality Assurance"
    )

    # Given the STX blog page is displayed
    blog_page.load()

    # And the cookie consent button is accepted

    blog_page.cookie_consent_button.click()

    # When the user searches for a phrase
    blog_page.search.click()
    blog_page.search.fill(keyword)
    blog_page.search.press("Enter")

    # Then a popup with search results is displayed
    expect(blog_page.main_popup).to_be_visible()

    # And the search results have a count of 4

    expect(blog_page.headings).to_have_count(4)

    # And the search results contain the article title

    expect(blog_page.headings.filter(has_text=article_title)).to_be_visible()
