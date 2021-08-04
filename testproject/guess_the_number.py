from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"

# Oldal betöltése
driver.get(URL)

number_value = [-19, 255]

# A visszajelzés szöveg elemei
deviation_l = driver.find_element_by_xpath('//p[text()="Guess lower."]')
deviation_h = driver.find_element_by_xpath('//p[text()="Guess higher."]')
deviation_y = driver.find_element_by_xpath('//p[text()="Yes! That is it."]')

# Elemek, gombok megkeresése
input_number = driver.find_element_by_xpath("//input")
guess = driver.find_element_by_xpath('//button[text()="Guess"]')
restart = driver.find_element_by_xpath('//button[text()="Restart"]')
input_number.send_keys(1)
guess.click()

i = 1
while deviation_y != "Yes! That is it.":
    if deviation_h.text == "Guess higher.":
        input_number.clear()
        input_number.send_keys(i)
        i += 1
        #time.sleep(1)
        guess.click()
    else:
        break
assert i == int(driver.find_element_by_xpath('//span[@class="badge ng-binding"]').text)


time.sleep(3)
restart.click()
# Teszt a -19-es számmal
input_number.send_keys(number_value[0])
guess.click()
assert deviation_h.text == "Guess higher."

input_number.clear()
restart.click()

# Teszt a 255-es számmal
input_number.send_keys(number_value[1])
guess.click()
assert deviation_l.text == "Guess lower."


driver.close()
