from playwright.sync_api import Page


class STXBlogPage:
    URL = '/blog'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search = page.get_by_role("textbox", name="search")
        self.main_popup = page.locator(".popupBoxSearchBox")


    def load(self) -> None:
        self.page.goto(self.URL)