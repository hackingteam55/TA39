# pip install selenium
# pip install webdriver-manager

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
# maximizam fereastra
driver.maximize_window()

# navigam catre un url
driver.get('https://formy-project.herokuapp.com/form')


#selector by ID
try:
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys('Matei')
except Exception as e:
    print('ID-ul introdus nu este corect')
print('Am ajuns aici')
# driver.find_element(By.ID, 'first-name').send_keys('TEST AUTOMATION')

sleep(10)
# inchidem fereastra de chrome
driver.quit()




