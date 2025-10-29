from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Needed for CI environments
    options.add_argument("--disable-dev-shm-usage")  # Prevent resource issues
    options.add_argument("--disable-gpu")  # Disable GPU rendering
    options.add_argument("--window-size=1920,1080")  # Optional: Set window size

    driver = webdriver.Chrome(options=options)
    return driver
