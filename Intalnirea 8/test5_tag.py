from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()

#navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

sleep(5)
#selector by TAG cand e unul singur
chrome.find_element(By.TAG_NAME, 'input').click()
sleep(5)
#daca gasim mai multe, le punem intr-o lista
input_list = chrome.find_elements(By.TAG_NAME, 'input')
#print(input_list)
input_list[0].send_keys('Alexandru Ioan Cuza')
input_list[1].click()

sleep(5)
chrome.quit()