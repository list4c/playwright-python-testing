from playwright.sync_api import Page

from pages.locators.main_page_locators import MainPageLocators
from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.banner_title = self.page.locator(MainPageLocators.BANNER_TITLE)
