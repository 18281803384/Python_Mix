import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 尝试传参
s = Service('C:\Program Files\Google\Chrome\Application/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.baidu.com/')
time.sleep(5)
driver.quit()
