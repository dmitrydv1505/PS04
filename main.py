from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time


browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

assert "Википедия" in browser.title
search_box = browser.find_element(By.ID, value="searchInput")
search_box.send_keys("Солнечная система")
time.sleep(5)

search_box.send_keys(Keys.RETURN)

time.sleep(5)
a = browser.find_element(By.LINK_TEX, value="Cолнечная система")
a.click()
