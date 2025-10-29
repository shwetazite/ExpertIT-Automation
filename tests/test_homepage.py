def test_open_homepage(driver):
    driver.get("https://www.expertit.in")
    title = driver.title
    assert "Expert IT" in title, f"Expected 'Expert IT' in title, but got: {title}"
