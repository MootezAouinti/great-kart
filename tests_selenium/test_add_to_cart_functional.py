from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


@pytest.mark.functional
def test_add_to_cart_functional():
    # ✅ Setup Chrome WebDriver
    service = Service("C:/Users/Mootaz Aouinti/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # 1️⃣ Open the store page
        driver.get("http://127.0.0.1:8000/store/")
        driver.maximize_window()

        # 2️⃣ Wait until the first product link is visible and click it
        product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.title"))
        )
        product.click()
        time.sleep(2)

        # 3️⃣ Select color and size if available
        try:
            color_dropdown = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.NAME, "color"))
            )
            color_dropdown.click()
            color_dropdown.find_element(By.XPATH, "//option[2]").click()
        except:
            print("⚠️ No color selection found")

        try:
            size_dropdown = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.NAME, "size"))
            )
            size_dropdown.click()
            size_dropdown.find_element(By.XPATH, "//option[2]").click()
        except:
            print("⚠️ No size selection found")

        # 4️⃣ Click the Add to Cart button (corrected selector)
        add_to_cart_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and .//span[text()='Add to Cart']]"))
        )
        add_to_cart_btn.click()
        time.sleep(3)

        # 5️⃣ Verify that cart page loaded
        assert "Checkout" in driver.page_source or "Grand Total" in driver.page_source
        print("✅ Product successfully added to cart and verified!")

    finally:
        driver.quit()
