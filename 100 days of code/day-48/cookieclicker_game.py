from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load
sleep(3)

# Handle language selection
print("Looking for language selection...")
try:
    language_button = driver.find_element(By.ID, "langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3)  # Wait for the game to load
except NoSuchElementException:
    print("Language selection not found.")

# Handle cookie consent
try:
    consent_button = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
    consent_button.click()
    print("Accepted cookie consent.")
    sleep(1)
except NoSuchElementException:
    print("No cookie consent banner found.")

# Locate the big cookie
cookie = driver.find_element(By.ID, "bigCookie")

# List of item IDs
item_ids = [f"product{i}" for i in range(18)]

# Timers
wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5  # Run for 5 minutes

while True:
    cookie.click()

    # Every 5 seconds, try to buy the most expensive item we can afford
    if time() > timeout:
        try:
            # Get current cookie count
            cookies_element = driver.find_element(By.ID, "cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # Get all store products
            products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")

            # Buy the most expensive affordable item
            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or store items.")

        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, "cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count.")
        break
