from playwright.sync_api import Page

from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
