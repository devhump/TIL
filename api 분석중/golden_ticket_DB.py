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



def get_playIds_list():
    URL = (
        "http://www.kopis.or.kr/openApi/restful/pblprfr?service="
        + SECRET_KEY + stdate + eddate + cpage + rows
    )

    print(URL)

    response = requests.get(URL)
    # print(URL)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, "xml")  # xml 문서라서
    playIds = soup.find_all("mt20id") # mt20id : 목록 태그

    playIds_list = []
    for id in playIds:

        playIds_list.append(id.get_text())

    return playIds_list


def get_play_info():
    cnt = 0
    for playId in get_playIds_list():
        cnt += 1

        URL = (
            "http://www.kopis.or.kr/openApi/restful/pblprfr/" 
            + playId + "?service=" + SECRET_KEY
        )
        response = requests.get(URL)

        print(URL)
        soup = BeautifulSoup(response.text, "xml")
        title = soup.find("prfnm")
        a = title.get_text()
        print(a)

        if cnt == 1:
            break



get_play_info()
