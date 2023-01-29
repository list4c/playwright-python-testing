from playwright.sync_api import Page


class STXMainPage:
    URL = '/'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.blog_button = page.get_by_role("menuitem", name="Blog").nth(0)


    def load(self) -> None:
        self.page.goto(self.URL)