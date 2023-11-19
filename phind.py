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

op = webdriver.ChromeOptions()
op.binary_location='/usr/bin/google-chrome-stable'
op.add_argument(f"user-agent={UserAgent.random}")
op.add_argument("user-data-dir=./")
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = uc.Chrome(chrome_options=op)

driver.get('https://www.phind.com/')

def send_prompt(prompt):
       inputElements = driver.find_elements(By.TAG_NAME, "textarea")
       inputElements[0].clear()
       inputElements[0].send_keys(prompt)

       driver.find_element(By.CLASS_NAME,"fe-search").click()

       loading = True
       while loading:
              try:
                     uppercases = driver.find_elements(By.CLASS_NAME,"text-uppercase")
                     for u in uppercases:
                            if u.text=='SUGGESTIONS':
                                   loading = False
                                   break
              except:
                     pass

       result = ''

       for div in driver.find_elements(By.CLASS_NAME,"fs-5"):
              result += div.get_attribute('outerHTML')
              # result += div.text
              
       print(result)
       return result

       driver.close()
       driver.quit()
