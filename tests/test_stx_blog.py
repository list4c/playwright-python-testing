from playwright.sync_api import Page, expect


def test_blog_page_and_filter_articles(page: Page, stx_page, blog_page):
    expected_link = "Moderated and Unmoderated Remote Usability Testing: What Is It, How to Run It, and " \
                    "What Are the Benefits?"
    search_query = "test"

    stx_page.load()
    stx_page.accept_cookies()
    stx_page.open_blog()
    blog_page.search_articles(search_query)

    expect(blog_page.get_searched_link(expected_link)).to_be_visible()
    expect(blog_page.get_searched_posts).to_have_count(4)
