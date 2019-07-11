from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.nu.nl")

button = driver.find_element_by_id("sanoma-consent-accept-button")
button.click()

article = driver.find_element_by_link_text("Merkel ontkent gezondheidsproblemen na derde trilaanval")# this text is not exist right now, so search by text is not relayable(if text change)
article.click()

# you can reuse previosly created browser instance and directly call 'driver.get("YOUR URL")'

driver.get("https://www.bbc.com/")

search_input = driver.find_element_by_id("orb-search-q")
search_input.send_keys("Trump")
search_button = driver.find_element_by_id("orb-search-button")
search_button.click()

#article = driver.find_element_by_link_text("Panorama: Trump: Is the President a Sex Pest?")
article = driver.find_element_by_xpath("/html/body/div[6]/section[2]/ol/li[3]/article/div/h1/a") # it would be better to avoid using "GENERATED xpaths" because they are rely on static page structure
article.click()

driver.quit()
