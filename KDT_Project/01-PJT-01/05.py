import json
from pprint import pprint

movie_info_idx = ['id', 'title', 'vote_average', 'overview']
movie_info_dict = {}

def movie_info(movie, genres):

    for i in range(len(movie_info_idx)):
        for j in movie:
            if movie_info_idx[i] == j:
                movie_info_dict[movie_info_idx[i]] = movie.get(j)

    #반복문 내 임시값 저장을 위해 빈 딕셔너리, 리스트 각각 생성
    temp_dict = {}
    temp_list = []

    for a in range(len(genres_list)):
        temp_dict = genres_list[a] 
        # genres_list 내 각 값이 딕셔너리형태인것에 착안
        # 값을 조작하기 위해 딕셔너리로 변환

        if temp_dict['id'] in movie['genre_ids']: # id 확인을 통해 코드가 같으면
            temp_list.append(temp_dict["name"]) # 해당 장르 이름을 불러와 새 리스트에 저장

            movie_info_dict["genres_name"] = temp_list 
            # genres_name 이라는 키값에 임시 리스트 내용을 val 값으로 매핑 후 저장 
            
    return movie_info_dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))