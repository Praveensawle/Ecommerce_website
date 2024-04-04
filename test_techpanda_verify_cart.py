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

def test_verify_cart(driver):
    expected_product = "SONY XPERIA"  # Replace with the product name 
    # Navigate to the home page
    driver.get("http://live.techpanda.org/index.php/customer/account/")  # 
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("user@gmail.com")
        # Password field
    driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("123456")
        # Click login button
    driver.find_element(By.XPATH,"//button[@id='send2']").click()
    
    # Find the cart icon and click on it
    cart_icon = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//header/div[1]/div[2]/div[1]/div[1]/a[1]")))
    cart_icon.click()
    
    # Find all products in the cart
    cart_items = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-name')))
    
    # Extract the product names from the cart items
    cart_product_names = [item.text for item in cart_items]
    
    # Assert that the expected product is in the cart
    assert expected_product in cart_product_names, f"Expected product '{expected_product}' not found in the cart."
    
    print("Cart verification successful.")
    time.sleep(5)
if __name__ == "__main__":
    pytest.main()
