from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.mark.functional
def test_checkout_functional():
    service = Service("C:/Users/Mootaz Aouinti/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # Log in first
        driver.get("http://127.0.0.1:8000/accounts/login/")
        driver.maximize_window()

        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        password = driver.find_element(By.NAME, "password")

        email.send_keys("testuser@gmail.com") 
        password.send_keys("Password@123")
        password.submit()
        time.sleep(2)

        # Go to store
        driver.get("http://127.0.0.1:8000/store/")
        time.sleep(1)

        # Click the first product
        product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.title"))
        )
        product.click()

        # Select options if available
        try:
            color = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "color")))
            color.click()
            color.find_element(By.XPATH, "//option[2]").click()
        except:
            print("⚠️ No color option found")

        try:
            size = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "size")))
            size.click()
            size.find_element(By.XPATH, "//option[2]").click()
        except:
            print("⚠️ No size option found")

        # Add to cart
        add_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add')]"))
        )

        add_btn.click()
        time.sleep(2)

        # Go to cart and click Checkout
        driver.get("http://127.0.0.1:8000/cart/")
        time.sleep(2)

        checkout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart/checkout/']"))
        )
        checkout_btn.click()
        time.sleep(3)

        # Fill checkout fields
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "first_name"))).send_keys("Mootaz")
        driver.find_element(By.NAME, "last_name").send_keys("Aouinti")
        driver.find_element(By.NAME, "email").send_keys("testuser@gmail.com")
        driver.find_element(By.NAME, "phone").send_keys("26414032")
        driver.find_element(By.NAME, "address_line_1").send_keys("Rue Jelouli Fares")
        driver.find_element(By.NAME, "address_line_2").send_keys("Nabeul")
        driver.find_element(By.NAME, "city").send_keys("Nabeul")
        driver.find_element(By.NAME, "state").send_keys("Nabeul")
        driver.find_element(By.NAME, "country").send_keys("Tunisia")
        driver.find_element(By.NAME, "order_note").send_keys("Please deliver quickly")

        # Click Place Order
        place_order_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @name='submit']"))
        )
        place_order_btn.click()
        time.sleep(3)

        # Verify redirect or confirmation
        assert "Order" in driver.title or "Thank you" in driver.page_source or "Payment" in driver.page_source

    finally:
        driver.quit()
