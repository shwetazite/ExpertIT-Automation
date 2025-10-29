from pages.homepage import HomePage

def test_open_homepage(driver):
    home = HomePage(driver)
    home.open()
    assert "ExpertIT" in home.get_title()
