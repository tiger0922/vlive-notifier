from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

vliveNum = input("Please input video ID: ")
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get('https://www.vlive.tv/video/' + vliveNum)
delay = 3
# vliveNum = input("Please Enter the video id: ") 

try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_rmc_ly_inner')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
for tag in soup.find_all("span", class_='u_rmc_lang'):
    print(tag.text)
        
# soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.find_all('span', class_="u_option_select"))
