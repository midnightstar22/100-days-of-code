from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")


# price_dollar=driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents=driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text},{price_cents.text}")

# search_bar=driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button=driver.find_element(By.ID, value="submit")
# print(button.size)
documentation_link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# print(documentation_link.text)
# driver.close()

bug_link=driver.find_element(By.XPATH,value='//*@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

tier_1= driver.find_element(By.CLASS_NAME,value="tier-1")

event_times= driver.find_element(By.CSS_SELECTOR, value=".event-widget time")

event_names= driver.find_element(By.CSS_SELECTOR, value=".event-widget li a")

events={}

for n in range(len(event_times)):
    events[n]={
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.quit()