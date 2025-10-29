class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.expertit.in/"
        def open(self):
            self.driver.get(self.url)

        def get_title(self):
            return self.driver.title
        def click_services(self):
            el = self.driver.find_element("link text", "Services")
            el.click()