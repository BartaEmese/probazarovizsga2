from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"

# Oldal betöltése
driver.get(URL)
time.sleep(3)

# Filmek listája
container_movies = driver.find_elements_by_xpath("//div[@class='container-movies']")
# Ellenőrizzük a filmek darabszámát
assert len(container_movies) == 24

# Tesztadat:
# Film title: Black widow
# Release year: 2021
# Chronological year of events: 2020
# Trailer url: https://www.youtube.com/watch?v=Fp9pNPdNwjI
# Image url: https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg
# Film summary: https://www.imdb.com/title/tt3480822/

# új film felvétele
register = driver.find_element_by_xpath("//button[text()='Register']").click()
time.sleep(2)
film_title = driver.find_element_by_id("nomeFilme").send_keys("Black widow")
relase_year = driver.find_element_by_id("anoLancamentoFilme").send_keys("2021")
chronological_year_of_events = driver.find_element_by_id("anoCronologiaFilme").send_keys("2020")
trailer_url = driver.find_element_by_id("linkTrailerFilme").send_keys("https://www.youtube.com/watch?v=Fp9pNPdNwjI")
image_url = driver.find_element_by_id("linkImagemFilme").send_keys("https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg")
film_summary_url = driver.find_element_by_id("linkImdbFilme").send_keys("https://www.imdb.com/title/tt3480822/")
save_button = driver.find_element_by_xpath("//button[text()='Save']").click()
time.sleep(2)

# Vizsgáljuk
container_movies = driver.find_elements_by_xpath("//div[@class='container-movies']")
# Ellenőrizzük a filmek darabszámát
assert len(container_movies) == 25
time.sleep(2)

driver.close()
