from playwright.sync_api import Page


class BasePage:
    URL: str

    def __init__(self, page: Page) -> None:
        self.page = page
        self.cookie_consent_button = page.get_by_role("button", name="Accept")

    def load(self) -> None:
        self.page.goto(self.URL)

    def accept_cookies(self):
        self.cookie_consent_button.click()
