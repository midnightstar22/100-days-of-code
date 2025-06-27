from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Wikipedia Main Page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Get the article count element (currently not clicked)
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()  # Uncomment this to click the link

# Get the "Content portals" link
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()  # Uncomment to navigate

# Search for "Python"
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)
