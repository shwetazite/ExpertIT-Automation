class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.expertit.in/"

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
