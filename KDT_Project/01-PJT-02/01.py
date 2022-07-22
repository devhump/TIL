import requests
from pprint import pprint


def popular_count():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key="
    response = requests.get(url).json() # 먼저 출력 후 json 구조 파악

    # 키 'result'의 val 값에 원하는 결과값 있는 것 확인 
    pop_movies = response["results"] # 인기있는 영화들의 딕셔너리들로 이뤄진 리스트  
    num = len(pop_movies)
    
    return num


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
