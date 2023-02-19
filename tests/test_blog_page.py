from playwright.sync_api import expect

from pages.page_objects.blog_page import BlogPage


def test_blog_page_and_filter_articles(blog_page: BlogPage):
    article_title = (
        "The Business Manager’s Guide to Software Testing and Quality Assurance"
    )
    search_query = "test"

    blog_page.load()
    blog_page.accept_cookies()
    blog_page.search_articles(search_query)

    expect(blog_page.main_popup).to_be_visible()
    expect(blog_page.get_searched_link(article_title)).to_be_visible()
    expect(blog_page.get_searched_posts).to_have_count(4)
