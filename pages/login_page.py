from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.expertit.in/login"  # Change if actual login URL differs
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "loginBtn")

    def open(self):
        self.driver.get(self.url)

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

    def verify_login_result(self):
        return "Dashboard" in self.driver.title or "Invalid" in self.driver.page_source
