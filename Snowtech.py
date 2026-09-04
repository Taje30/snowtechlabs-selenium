from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome() # Open Chrome
driver.maximize_window() # Maximize browser
driver.get("https://snowtechlabs.com/") # Open website
driver.save_screenshot("01_homepage.png")
get_started = driver.find_element(
    By.XPATH,
    "//a[span[text()='Get Started']]" # Click "Get Started"
)

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    get_started
)

time.sleep(1)
get_started.click()

name_field = driver.find_element(By.NAME, "name")
name_field.send_keys("Tajpreet Singh")

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("taj@bmo.com")

company_field = driver.find_element(By.NAME, "company")
company_field.send_keys("BMO")

phone_field = driver.find_element(By.NAME, "phone")
phone_field.send_keys("2268997301")

message_field = driver.find_element(By.NAME, "message")
message_field.send_keys("I have an enquiry, call me")

budget = driver.find_element(By.NAME, "budget")


driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    budget
)

time.sleep(1)


driver.execute_script(
    "arguments[0].focus();",
    budget
)

# Move slider to minimum = $1,000
budget.send_keys(Keys.HOME)

# Move right 12 times
# 1000 + (12 × 500) = 7000
for i in range(12):
    budget.send_keys(Keys.ARROW_RIGHT)

# Verify budget
print("Budget selected:", budget.get_attribute("value"))

send_button = driver.find_element(
    By.XPATH,
    "//button[span[text()='Send Message']]"
)
driver.save_screenshot("send message.png")

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    send_button
)

time.sleep(1)


send_button.click()
time.sleep(5)
driver.save_screenshot("confirmation.png")
time.sleep(10)

driver.quit()