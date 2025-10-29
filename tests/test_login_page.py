from pages.login_page import LoginPage

def test_login(driver):
    driver.get("https://www.expertit.in/login")  # <-- Use actual login page URL
    login = LoginPage(driver)
    login.login("test_user", "password123")
    assert "Dashboard" in driver.title
