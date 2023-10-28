from playwright.sync_api import Page

from pages.locators.base_page_locators import BasePageLocators


class BasePage:
    URL: str

    def __init__(self, page: Page) -> None:
        self.page = page

        self.cookie_consent_button = page.locator(BasePageLocators.COOKIE_ALLOW_ALL)

    def load(self) -> None:
        self.page.goto(self.URL)

    def accept_cookies(self):
        self.cookie_consent_button.click()

    def load_and_accept_cookies(self):
        self.load()
        self.accept_cookies()
