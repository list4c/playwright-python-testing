from playwright.sync_api import Page

from pages.page_objects.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.blog_btn = page.locator(MainPageLocators.HEADER_LINK).filter(has_text="Blog")
        self.accept_cookies_btn = page.get_by_role(**MainPageLocators.BUTTON_ACCEPT_COOKIES)

    def open_blog(self) -> None:
        self.blog_btn.click()

    def accept_cookies(self) -> None:
        self.accept_cookies_btn.click()
