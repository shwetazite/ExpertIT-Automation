def test_open_homepage(driver):
    driver.get("https://www.expertit.in/")
    assert "Expert" in driver.title
