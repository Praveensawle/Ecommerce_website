from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class EcommercePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_website(self, url):
        self.driver.get(url)

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH,"//input[@id='email']")
        password_field = self.driver.find_element(By.XPATH,"//input[@id='pass']")
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def add_product_to_cart(self, product_name):
        search_bar = self.driver.find_element(By.ID, 'search')
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)
        product_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'" + product_name + "')]")))
        product_link.click()
        add_to_cart_button = self.driver.find_element(By.ID, 'add-to-cart')
        add_to_cart_button.click()

    def go_to_home_page(self):
        home_page_link = self.driver.find_element(By.CSS_SELECTOR, 'a.logo')
        home_page_link.click()

    def verify_cart_on_home_page(self, product_name):
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart-item')
        for item in cart_items:
            if product_name in item.text:
                return True
        return False

    def complete_shopping_process(self, username, password, product_name, website_url):
        self.navigate_to_website(website_url)
        self.login(username, password)
        self.add_product_to_cart(product_name)
        self.go_to_home_page()
        return self.verify_cart_on_home_page(product_name)

# Test functions outside of the class definition
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping_process(driver):
    username = "user@gmail.com"
    password = "123456"
    product_name = "product_to_add"
    website_url = "http://live.techpanda.org/index.php/"

    ecommerce_page = EcommercePage(driver)
    cart_verification_result = ecommerce_page.complete_shopping_process(username, password, product_name, website_url)
    assert cart_verification_result == True
