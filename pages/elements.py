class TextInput:
    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        text_input = obj.page.locator(self.locator)
        text_input.clear()
        text_input.fill(value)
