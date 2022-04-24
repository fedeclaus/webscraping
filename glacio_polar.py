from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
import requests
import wget


url = ('https://www.polarview.aq/tablelisting/sar')
driver = webdriver.Chrome()
driver.get(url)

select = Select(driver.find_element_by_name('area'))
# select by visible text
select.select_by_visible_text('Antarctic Peninsula')
element = driver.find_element_by_name("search")
ActionChains(driver).click(element).perform()
time.sleep(3)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
#dom = etree.HTML(str(soup))

"""
for link in soup.find_all('a', href=True):
    print(link['href'])
"""

for link in soup.find_all('a', href=True):
    if link['href'].startswith("https://www.polarview.aq/images/111_S1jpeg2000/"):
        print(link['href'])
        response = wget.download(link['href'])

driver.quit()