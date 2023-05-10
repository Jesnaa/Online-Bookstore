import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\jesna\OneDrive\Documents\Bookstore-C\BookStore\bookstore\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("http://127.0.0.1:8000/login/login/")

# Locate the username and password fields and input the credentials
username_field = driver.find_element(By.NAME, "email")
username_field.send_keys("jesnamol1112@gmail.com")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Jesna@123")

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load and check for the presence of the dashboard element
dashboard_element = driver.find_element(By.XPATH, "//h3[contains(text(), 'Horror')]")

# driver.get("http://127.0.0.1:8000/product")

driver.get("http://127.0.0.1:8000/addcart/1")

product_addcart = driver.find_element(By.XPATH, "//h3[contains(text(), 'Categories')]")

if product_addcart:
    print("Test Passed")
else:
    print("Test Failed")

# driver.get("http://127.0.0.1:8000/cart")

# Close the browser
driver.quit()