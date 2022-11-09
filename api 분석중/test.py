import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")

URL = (
    "http://www.kopis.or.kr/openApi/restful/pblprfr?service="
    + SECRET_KEY
    + "&stdate=20160601&eddate=20160630&cpage=1&rows=5&prfstate=02&signgucode=11&signgucodesub=1111&kidstate=Y"
)

response = requests.get(URL)

print(response.status_code)
# # print(response.content)
# # html = response.text
# soup = BeautifulSoup(response.text, "xml")  # xml 문서라서
# # title = soup.select("prfnm")#둘다 가능
# title = soup.find("prfnm")
# open_date = soup.find("prfpdfrom")
# close_date = soup.find("prfpdto")
# images = soup.find_all("styurl")

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
