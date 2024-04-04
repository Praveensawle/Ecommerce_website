from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# Initialize the Firefox WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage 
def test_setup():
    driver.get("http://live.techpanda.org/index.php/")

# login with username and password
def test_login():
   
        # Click on the Account button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/div[1]/div[2]/div[1]/a[1]/span[2]"))).click()
        time.sleep(2)  # Optional: Add a small delay to ensure the element is fully loaded
        # Click on Login button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Log In')]"))).click()
        time.sleep(2)
        print("Login button clicked successfully.")
        # Email field
        driver.find_element(By.XPATH,"//input[@id='email']").send_keys("user@gmail.com")
        # Password field
        driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("123456")
        # Click login button
        driver.find_element(By.XPATH,"//button[@id='send2']").click()


    



# Run the test setup
test_setup()

# Run the login test
test_login()
