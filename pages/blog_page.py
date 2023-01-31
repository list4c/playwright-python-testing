from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators import BlogPageLocators


class StxBlogPage(BasePage):
    URL = "/blog"

    def __init__(self, page: Page) -> None:
        super(StxBlogPage, self).__init__(page)
        self.cookie_consent_button = page.get_by_role("button", name="Accept")
        self.search = page.get_by_role("textbox", name="search")
        self.main_popup = page.locator(BlogPageLocators.MAIN_POPUP)
        self.headings = page.locator(BlogPageLocators.HEADINGS).get_by_role("heading")
