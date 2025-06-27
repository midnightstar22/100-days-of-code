from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL="midnightstar22072004@gmail.com"
PASSWORD="Marcomarco2223!"
PHONE="5893420842"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Go to the login page first
driver.get("https://www.linkedin.com/login")
time.sleep(3)

# Use IDs or correct selectors
email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD, Keys.ENTER)



time.sleep(5)  # Let the page load after login

# Now go to search results
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4253125999&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
        # Click Apply Button
    apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
    apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
    time.sleep(5)
    phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
    if phone.text == "":
        phone.send_keys(PHONE)

        # Check the Submit Button
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
    if submit_button.get_attribute("data-control-name") == "continue_unify":

        print("Complex application, skipped.")
        continue
    else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

    time.sleep(2)




time.sleep(5)
driver.quit()