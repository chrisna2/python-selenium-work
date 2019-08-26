from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import requests
import xlsxwriter


def srch_google_map(key):
    # 백그라운드에서 실행하도록 설정
    print("검색을 시작합니다! 검색어 : " + key)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=640x480')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('./chromedriver.exe', options=options)
    print("검색중 입니다....(1/5)")
    driver.implicitly_wait(3)
    driver.get('https://www.google.co.kr/maps/@37.053745,125.6553969,5z?hl=ko')
    print("검색중 입니다....(2/5)")
    time.sleep(3)
    srch_input = driver.find_element_by_id('searchboxinput')
    srch_input.send_keys(key)
    print("검색중 입니다....(3/5)")
    time.sleep(4)
    srch_input.send_keys(Keys.ENTER)
    print("검색중 입니다....(4/5)")
    time.sleep(3)
    driver.get_screenshot_as_file(
        'D:\\tyn_dev\\workspace_pycham\\python-selenium-work\\image2\\screen-shot.png')
    print("검색중 입니다....(5/5)")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    print("검색이 완료되었습니다!")

    result_list = []
    local_img_lst = []
    print("파싱 및 이미지 저장 중입니다....")
    img_rex = re.compile(r'''\(([^)]+)''', re.VERBOSE)

    idx = 0
    for div_info in soup.select('#pane > div > div.widget-pane-content.scrollable-y > div > div > div.section-layout.section-scrollbox.scrollable-y.scrollable-show.section-layout-flex-vertical > div > div.section-result-content'):
        name = div_info.select_one('div.section-result-text-content > div.section-result-header > div.section-result-title-container > h3 > span').text.strip()
        location = div_info.select_one('div.section-result-text-content > div:nth-child(2) > span.section-result-location').text.strip()
        images = img_rex.findall(div_info.select_one('div.section-image-container > div')['style'])[0]

        if images[0:6] != 'https:':
            images = 'https:' + images

        res = requests.get(images)
        with open('./image2/' + re.sub(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', name) + ".png", 'wb') as file:
            file.write(res.content)
            local_images = "D:\\tyn_dev\\workspace_pycham\\python-selenium-work\\image2\\" + re.sub(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', name) + ".png"

        result_list.append([name, location, None])
        local_img_lst.append([images, local_images])
        idx += 1
        print(idx.__str__()+"건의 데이터가 파싱되었습니다.")

    print(result_list)

    print("파싱된 데이터를 엑셀로 저장 중 입니다.")
    df = pd.DataFrame(result_list)
    df.columns = ["상호명", "주소", "이미지"]
    df.isna

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('./excel/'+key+'.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    for i in range(result_list.__len__()):
        worksheet.insert_image('C' + (i + 2).__str__(), local_img_lst[i][1])

    writer.save()
    print("엑셀 변환 완료 : 로직이 완료 되었습니다.")


def main():
    key = input("찾으실 검색어를 입력해 주세요 : ")
    srch_google_map(key)


main()