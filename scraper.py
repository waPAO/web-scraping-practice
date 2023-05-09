import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver_service = Service(executable_path='/Users/paolosigua/Downloads/chromedriver_mac64/chromedriver')
driver = webdriver.Chrome(options=options, service=driver_service)
driver.get('https://www.target.com/')