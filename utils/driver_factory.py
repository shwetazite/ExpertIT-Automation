import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(headless=False):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    # ✅ Use a unique temporary user data directory for GitHub Actions
    temp_user_data = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_user_data}")

    if headless:
        options.add_argument("--headless=new")  # Chrome 109+ new headless mode

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver
