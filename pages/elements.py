class SearchInput:
    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        obj.page.locator(self.locator).type(value, delay=400)
