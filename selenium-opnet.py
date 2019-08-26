from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time


driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://www.opinet.co.kr/searRgSelect.do')
time.sleep(1)
driver.get('http://www.opinet.co.kr/searRgSelect.do')

time.sleep(3)

sido_select = Select(driver.find_element_by_id('SIDO_NM0'))
sido_select.select_by_visible_text('부산')
time.sleep(0.5)

sigungu_select = Select(driver.find_element_by_id('SIGUNGU_NM0'))
sigungu_select.select_by_visible_text('해운대구')
time.sleep(3)

# 파싱용 데이터 추출

driver.get_screenshot_as_file('D:\\tyn_dev\\workspace_pycham\\python-selenium-work\\image\\screen-shot.png')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup)


# 파싱 (herf 값 파싱 : attribute 값)
href_value = soup.select_one('#body1 > tr:nth-child(16) > td.rlist > a')['href']
print(href_value)
print(href_value.split(',')[22][1:-1])

driver.close()
# [참고] https://github.com/soongon/py-scraping-201901