import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC

def translate(prompt, sk, tk):
       op = webdriver.ChromeOptions()
       op.binary_location='/usr/bin/google-chrome-stable'
       op.add_argument(f"user-agent={UserAgent.random}")
       op.add_argument("user-data-dir=./")
       op.add_experimental_option("detach", True)
       op.add_experimental_option("excludeSwitches", ["enable-logging"])

       driver = uc.Chrome(chrome_options=op)
       driver.get('https://papago.naver.com/?sk='+sk+'&tk='+tk)
       result = ''

       while True:
              inputElements = driver.find_elements(By.TAG_NAME, "textarea")
              if len(inputElements) != 0:
                     break

       inputElements[0].send_keys(prompt)
       sleep(5)

       while True:
              inputElements = driver.find_elements(By.ID, "txtTarget")
              if len(inputElements) != 0:
                     for i in inputElements:
                            result += i.text
                     break

       driver.quit()
       print('종료되었습니다.')
       return result