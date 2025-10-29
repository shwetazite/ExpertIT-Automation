import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [
    ("admin", "admin123"),
    ("user1", "wrongpass"),
    ("testuser", "test123")
])
def test_login_page(driver, username, password):
    page = LoginPage(driver)
    page.open()
    page.login(username, password)
    assert page.verify_login_result()
