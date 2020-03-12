from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import telebot
import time

vliveNum = input("Please input video ID: ")
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get('https://www.vlive.tv/video/' + vliveNum)
delay = 5

myElem = None
while myElem == None:
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_rmc_ly_inner')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        time.sleep(1800)
        browser.refresh()
        print("refresh: " + browser.current_url)

html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
title = soup.find("strong", class_='tit', attrs={'title':True})['title']
print(title)
for tag in soup.find_all("span", class_='u_rmc_lang'):
    print(tag.text)
    if tag.text == 'English':
        telebot.send_text(title + '\n' + 'English subtitle is ready!')
    elif '中文' in tag.text:
        telebot.send_text(title + '\n' + tag.text + '已更新')

