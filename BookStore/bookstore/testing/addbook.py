
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


service = Service(executable_path=r"C:\Users\jesna\OneDrive\Documents\Bookstore-C\BookStore\bookstore\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get("http://127.0.0.1:8000/login/login")

# Locate the username and password fields and input the credentials
username_field = driver.find_element(By.NAME, "email")
username_field.send_keys("bookrakbook@gmail.com")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Bookrak@123")

# Submit the login form
password_field.send_keys(Keys.RETURN)

driver.get("http://127.0.0.1:8000/add_book/")

# Fill in the form fields
book_name = driver.find_element(By.NAME, 'book_name')
book_name.send_keys('Puss In Boots')


category = Select(driver.find_element(By.NAME, 'book_category'))
category.select_by_value('9')


book_quantity = driver.find_element(By.NAME, 'book_quantity')
book_quantity.send_keys('20')


book_price = driver.find_element(By.NAME, 'book_price')
book_price.send_keys('187')


book_price = driver.find_element(By.NAME, 'book_oldprice')
book_price.send_keys('200')


book_author = driver.find_element(By.NAME, 'book_author')
book_author.send_keys('Charles Perrault')


book_year = driver.find_element(By.NAME, 'book_year')
book_year.send_keys('2015')


book_language = driver.find_element(By.NAME, 'book_language')
book_language.send_keys('English')



book_publisher = driver.find_element(By.NAME, 'book_publisher')
book_publisher.send_keys('SAGA Egmont')


book_desc = driver.find_element(By.NAME, 'book_desc')
book_desc.send_keys('Puss in Boots, is a European literary fairy tale about a cat who uses trickery and deceit to gain power wealth, and the hand of a princess in marriage for his penniless and low-born master.')




image_upload = driver.find_element(By.NAME, "img")
image_upload.send_keys(r"C:\Users\jesna\OneDrive\Documents\Bookstore-C\BookStore\bookstore\media\pics\puss_in_boots.png")


image_upload = driver.find_element(By.NAME, "img2")
image_upload.send_keys(r"C:\Users\jesna\OneDrive\Documents\Bookstore-C\BookStore\bookstore\media\pics\puss_in_boots_2.png")






# Submit the form
submit_button = driver.find_element('css selector', 'button[type="submit"]')
submit_button.click()

driver.get("http://127.0.0.1:8000/admin_book")


# Wait for the page to load and check for the presence of the dashboard element
dashboard_element = driver.find_element(By.XPATH, "//h4[contains(text(), 'Books')]")
if dashboard_element:
    print("Test Passed")
else:
    print("Test failed.")
