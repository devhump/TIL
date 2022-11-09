import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

#################################################
# 필수 값
#################################################

# .env 파일의 api 불러옴
load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")

#공연 시작일자
stdate = "&stdate=" + "20220601"
#공연 종료일자
eddate = "&eddate=" + "20230630"
#현재페이지
cpage = "&cpage=" + "1"
# 페이지당 목록 수
rows = "&rows=" + "5"


#################################################
# 선택 값
#################################################
# 공연 상태 코드
prfstate = "&prfstate=" + "02"
# 지역코드 (시도)
signgucode = "&signgucode=" + "11"
# 지역코드 (구군)
signgucodesub = "&signgucodesub=" + "1111"
# 아동공연여부
kidstate = "&kidstate" + "Y"

URL = (
    "http://www.kopis.or.kr/openApi/restful/pblprfr?service="
    + SECRET_KEY + stdate + eddate + cpage + rows
)

response = requests.get(URL)
print(URL)
# print(response.status_code)

# print(response.content)
# # html = response.text
soup = BeautifulSoup(response.text, "xml")  # xml 문서라서
# # title = soup.select("prfnm")#둘다 가능
# title = soup.find("prfnm")
# open_date = soup.find("prfpdfrom")
# close_date = soup.find("prfpdto")
images = soup.find_all("styurl")

# print(len(images))
# # print(images[0].get_text())
# # print(title)
# # a = title.contents[0]
# a = title.get_text()
# b = open_date.get_text()
# # c = images.get_text()


# print(a)
# print(b)
# # print(c)
# # print(len(c))
