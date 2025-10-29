from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_driver(browser="chrome"):
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Headless mode for CI
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")

        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
        return driver

    elif browser == "edge":
        return webdriver.Edge()

    elif browser == "firefox":
        return webdriver.Firefox()

    else:
        raise ValueError(f"Unsupported browser: {browser}")
