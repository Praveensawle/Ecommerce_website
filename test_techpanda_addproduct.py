import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_product_to_cart(driver):
    driver.get("http://live.techpanda.org/index.php/checkout/cart/")
    driver.find_element(By.XPATH, "//a[text()='Mobile']").click()

    # Wait for the "Add to Cart" button to be clickable
    wait = WebDriverWait(driver, 20)  # Adjust the timeout as needed
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='button btn-cart' and @title='Add to Cart'])[1]")))
    
    add_to_cart_button.click()
    time.sleep(5)

def test_go_to_homepage(driver):
    driver.get("http://live.techpanda.org/index.php/checkout/cart/")
    # Now 'driver' is accessible here
    wait = WebDriverWait(driver, 20)
    home_page_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//header/div[1]/a[1]/img[1]")))
    home_page_link.click()
