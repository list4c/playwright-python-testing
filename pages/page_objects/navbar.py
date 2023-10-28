import dataclasses

from playwright.sync_api import Page

from pages.elements import TextInput
from pages.locators.navbar_locators import NavbarLocators
from pages.page_objects.base_page import BasePage


@dataclasses.dataclass
class NavbarMenuOptions:
    SERVICES: str = 'Services'
    PORTFOLIO: str = 'Portfolio'
    TEAM: str = 'Team'
    RESOURCES: str = 'Resources'
    CAREERS: str = 'Careers'
    BLOG: str = 'Blog'
    CONTACT: str = 'Contact'

    def get_all_texts(self):
        return dataclasses.astuple(self)


class Navbar(BasePage):
    URL = '/'
    search_input = TextInput(NavbarLocators.SEARCH_INPUT)

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header_links = page.locator(NavbarLocators.HEADER_LINK)
        self.search_toggle = page.locator(NavbarLocators.SEARCH_TOGGLE)
        self.search_button = page.locator(NavbarLocators.SEARCH_BUTTON)
        self.search_results = page.locator(NavbarLocators.SEARCH_RESULTS)

    def get_navbar_links_formatted(self):
        headers = self.header_links.all()
        return {header.get_attribute('href').rstrip('/') for header in headers}

    def search_phrase(self, phrase):
        self.search_toggle.click()
        self.search_input = phrase
        self.search_button.click()

    def get_link(self, link_text):
        return self.header_links.filter(has_text=link_text)

    def go_to_link(self, link_text):
        self.get_link(link_text=link_text).click()
