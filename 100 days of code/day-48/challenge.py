from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Nakshaytra")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Nanma")

email = driver.find_element(By.NAME, "email")
email.send_keys("Python@gmail.com", Keys.ENTER)
