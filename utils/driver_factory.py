from selenium import webdriver

def get_driver(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
