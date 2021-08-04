from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"

# Oldal betöltése
driver.get(URL)

tipp = [10, 20]
deviation_l = driver.find_element_by_xpath('//p[text()="Guess lower."]')
deviation_h = driver.find_element_by_xpath('//p[text()="Guess higher."]')

input_number = driver.find_element_by_xpath("//input")
input_number.send_keys(tipp[0])
time.sleep(2)
guess = driver.find_element_by_xpath('//button[text()="Guess"]')
guess.click()
time.sleep(2)
if deviation_l == "Guess higher.":
    input_number = driver.find_element_by_xpath("//input").send_keys(tipp[1])
    guess.click()
elif deviation_h == "Guess higher.":
    input_number = driver.find_element_by_xpath("//input").send_keys(input_number.text - 1)



# number_of_guesses = driver.find_element_by_xpath('//span[@class="badge ng-binding"]')
# assert number_of_guesses.text ==
# driver.close()
