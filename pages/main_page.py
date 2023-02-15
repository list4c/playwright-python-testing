from playwright.sync_api import Page

from pages.base_page import BasePage


class StxMainPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super(StxMainPage, self).__init__(page)
        self.blog_button = page.get_by_role("menuitem", name="Blog").nth(0)
