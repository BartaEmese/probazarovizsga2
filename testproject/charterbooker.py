import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html"

# Oldal betöltése
driver.get(URL)

# Űrlap elemeinek megkeresése kitöltése
email_value = ["emese@gmail.com", "egmail"]
select = Select(driver.find_element_by_xpath('//select[@name="bf_totalGuests"]'))
select.select_by_visible_text('10')

button1 = driver.find_element_by_xpath('//button[@class="next-btn next-btn1"]')
button1.click()

date_input = driver.find_element_by_xpath('//input[@class="datepicker"]')
date_input.send_keys("2021-08-16")

select_time = Select(driver.find_element_by_xpath('//select[@name="bf_time"]'))
select_time.select_by_visible_text('Morning')

select_hours = Select(driver.find_element_by_xpath('//select[@name="bf_hours"]'))
select_hours.select_by_visible_text('4')

button2 = driver.find_element_by_xpath('//button[@class="next-btn next-btn2"]')
button2.click()

name = driver.find_element_by_xpath('//input[@name="bf_fullname"]')
name.send_keys("Barta Emese")

# Invalid email cím megadása
email = driver.find_element_by_xpath('//input[@name="bf_email"]')
email.send_keys(email_value[1])

request = driver.find_element_by_xpath('//button[@class="submit-btn"]')
request.click()
# A megjelenő figyelmeztető szöveg megjelenésének vizsgálata
email_error = driver.find_element_by_xpath('//span[@class="error"]')
assert email_error.text == "PLEASE ENTER A VALID EMAIL ADDRESS."

email.clear()
# Valid email cím megadása
email = driver.find_element_by_xpath('//input[@name="bf_email"]')
email.send_keys(email_value[0])


request = driver.find_element_by_xpath('//button[@class="submit-btn"]')
request.click()
# Helyer kitöltés esetén megjelenő szöveg vizsgálata
message = driver.find_element_by_id("booking-form")
assert message.text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."

driver.close()
