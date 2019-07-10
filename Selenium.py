import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.nu.nl")
time.sleep(2)

button = driver.find_element_by_id("sanoma-consent-accept-button")
button.click()
time.sleep(2)

article = driver.find_element_by_link_text("Merkel ontkent gezondheidsproblemen na derde trilaanval")
article.click()
time.sleep(2)

driver.quit()

driver = webdriver.Chrome()
driver.get("https://www.bbc.com/")
time.sleep(2)

search_input = driver.find_element_by_id("orb-search-q")
search_input.send_keys("Trump")
time.sleep(2)
search_button = driver.find_element_by_id("orb-search-button")
search_button.click()
time.sleep(2)

#article = driver.find_element_by_link_text("Panorama: Trump: Is the President a Sex Pest?")
article = driver.find_element_by_xpath("/html/body/div[6]/section[2]/ol/li[3]/article/div/h1/a")
article.click()
time.sleep(5)

driver.quit()
