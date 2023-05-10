
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

driver.get("http://127.0.0.1:8000/add_deliveryboy/")

# Fill in the form fields
username = driver.find_element(By.NAME, 'username')
username.send_keys('Akhil')


first_name = driver.find_element(By.NAME, 'first_name')
first_name.send_keys('Akhil')

last_name = driver.find_element(By.NAME, 'last_name')
last_name.send_keys('Raj')

email = driver.find_element(By.NAME, 'email')
email.send_keys('nehaharidas.m@gmail.com')

phonenumber = driver.find_element(By.NAME, 'phonenumber')
phonenumber.send_keys('9846358792')

hname = driver.find_element(By.NAME, 'hname')
hname.send_keys('Akhilam')

pincode = driver.find_element(By.NAME, 'pincode')
pincode.send_keys('670743')

city = driver.find_element(By.NAME, 'city')
city.send_keys('Idukky')


state = driver.find_element(By.NAME, 'state')
state.send_keys('Kerala')

country = driver.find_element(By.NAME, 'country')
country.send_keys('India')


# Submit the form
submit_button = driver.find_element('css selector', 'button[type="submit"]')
submit_button.click()
driver.get("http://127.0.0.1:8000/admin_delboy/")

# Wait for the page to load and check for the presence of the dashboard element
dashboard_element = driver.find_element(By.XPATH, "//h4[contains(text(), 'Delivery Boy List')]")
if dashboard_element:
    print("Test Passed")
else:
    print("Test failed.")
