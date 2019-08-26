import requests
from bs4 import BeautifulSoup
import re

# 1. 데이터 확보
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

res = requests.get('https://www.coupang.com/np/campaigns/82/components/178155', headers=headers)  # 쿠팡 > 가전

# 파이썬 문자열 모든 것을 문자열로 인식 시키려면 r'asda\ds\/\/\sad' 붙일 것
img_rex = re.compile(r'''src="\/\/.*\/thumbnails\/[^"]+\.jpg"''', re.VERBOSE)
# vs 코드 같은데서 검증한 정규식 가져오기

# 모든 패턴을 찾기 : findall
# 한개만 찾기 : search
pattern_matched = img_rex.findall(res.text)

img_customed = []
for pattern in pattern_matched:
    img_customed.append("http:"+pattern[5:-1])

print(img_customed)

for img in img_customed:
    res = requests.get(img)
    with open('./image/'+img[img.rindex('/'):], 'wb') as file:
        file.write(res.content)
        print(img+'_saved!')
