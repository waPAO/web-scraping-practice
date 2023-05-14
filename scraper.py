import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver_service = Service(executable_path='/Users/paolosigua/Downloads/chromedriver_mac64/chromedriver')
driver = webdriver.Chrome(options=options, service=driver_service)
driver.get('https://www.scrapethissite.com/pages/simple/')

results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(attrs={'class': 'col-md-4 country'}):
    name = element.find('h3')
    if name not in results:
      results.append(name.text)

for element in soup.findAll(attrs={'class': 'country-info'}):
    name = element.find('span')
    if name not in other_results:
      other_results.append(name.text)

series1 = pd.Series(results, name="Names")
series2 = pd.Series(other_results, name="Categories")
df = pd.DataFrame({'Names': series1, 'Categories': series2})
df.to_csv('names.csv', index=False, encoding='utf-8')

