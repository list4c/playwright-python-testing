from playwright.sync_api import Page

from pages.locators.main_page_locators import MainPageLocators
from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.blog_btn = page.locator(MainPageLocators.HEADER_LINK).filter(
            has_text="Blog"
        )
