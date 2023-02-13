from playwright.sync_api import expect

from pages.page_objects.blog_page import BlogPage
from pages.page_objects.main_page import MainPage


def test_blog_page_and_filter_articles(main_page: MainPage, blog_page: BlogPage):
    expected_link = (
        "Moderated and Unmoderated Remote Usability Testing: "
        "What Is It, How to Run It, and What Are the Benefits? "
    )
    search_query = "test"

    main_page.load()
    main_page.accept_cookies()
    main_page.open_blog()
    blog_page.search_articles(search_query)

    expect(blog_page.get_searched_link(expected_link)).to_be_visible()
    expect(blog_page.get_searched_posts).to_have_count(4)
