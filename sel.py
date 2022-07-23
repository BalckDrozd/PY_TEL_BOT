import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

ser = Service('/home/blackdrozd/PycharmProjects/pythonTB/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=ser, options=options)
driver.get('https://www.mail.ru/')
#time.sleep(1)
