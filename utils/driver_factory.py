import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(headless=False):
    options = Options()

    # ✅ Chrome stability flags for CI (GitHub Actions, Docker, etc.)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-debugging-port=9222")

    # ✅ Ensure Chrome uses a unique user data directory
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # ✅ Run headless in CI if requested
    if headless:
        options.add_argument("--headless=new")

    # ✅ Set Chrome binary location explicitly (for CI environments)
    # GitHub Actions has Chrome preinstalled here:
    options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver
