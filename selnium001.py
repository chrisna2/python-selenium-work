import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
# driver.get('http://www.naver.com')

# chromedriver 는 현재 사용하고 있는 크롬에 버전에 맞춰야 한다.
# 사용중인 크롬 버전 : 버전 76.0.3809.100(공식 빌드) (64비트)

driver.get("http://skgusrl2.cafe24.com/")

time.sleep(3)

driver.find_element_by_name('m_id').send_keys('admin01')
driver.find_element_by_name('m_pw').send_keys('1111')

time.sleep(3)

# 크롬 버튼에 해당하는 xpath 검색
driver.find_element_by_xpath('//*[@id="loginGo"]/div[3]/div[2]/input[2]').click()

time.sleep(5)

driver.close()
# 안해주면 브라우저가 계속 쌓인다.

'''
만약 CAPTCHA 가 걸리게 되면 해당 로직이 수행 되지 않는다.
'''
