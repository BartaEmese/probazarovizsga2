from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"

# Oldal betöltése
driver.get(URL)

elemek = []
with open('data.txt', 'r', encoding="UTF-8") as file:
    for row in file:
        elemek.append(row.strip())
print(elemek)

main_list = []
main = driver.find_elements_by_xpath('//li')
for i in main:
    main_list.append(i.text)
print(main_list)


driver.close()
