from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pytest

@pytest.mark.functional
def test_login_functional():
    # Setup Chrome WebDriver
    service = Service("C:/Users/Mootaz Aouinti/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # Open your local Django server
        driver.get("http://127.0.0.1:8000/accounts/login/")
        driver.maximize_window()
        time.sleep(2)

        # Fill email and password
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")

        email_input.send_keys("testuser@gmail.com")
        password_input.send_keys("Password@123")
        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        # Verify redirection to dashboard
        assert "Dashboard" in driver.page_source

    finally:
        driver.quit()
