from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"

# Oldal betöltése
driver.get(URL)

# Karakterek megkeresése
angel = driver.find_element_by_id("angel")
beast = driver.find_element_by_id("beast")
cyclops = driver.find_element_by_id("cyclops")
emma_frost = driver.find_element_by_id("emma-frost")
iceman = driver.find_element_by_id("iceman")
jean_grey = driver.find_element_by_id("jean-grey")
magneto = driver.find_element_by_id("magneto")
night_crawler = driver.find_element_by_id("nightcrawler")
professor_x = driver.find_element_by_id("professor-x")
psylocke = driver.find_element_by_id("psylocke")
quicksilver = driver.find_element_by_id("quicksilver")
rictor = driver.find_element_by_id("rictor")
storm = driver.find_element_by_id("storm")
sunspot = driver.find_element_by_id("sunspot")
tithe = driver.find_element_by_id("tithe")
wolverine = driver.find_element_by_id("wolverine")

# 1. szűrés Original X-Mem
original = driver.find_element_by_xpath("//label[@for='original']")
original.click()
time.sleep(1)
assert

# Megjelenő karakterek ellenőrzése



driver.close()
