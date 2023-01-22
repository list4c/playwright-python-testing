from playwright.sync_api import Page


class STXMainPage:
    URL = 'https://www.stxnext.com'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.blog_button = page.get_by_role("menuitem", name="Blog")

    def load(self) -> None:
        self.page.goto(self.URL)