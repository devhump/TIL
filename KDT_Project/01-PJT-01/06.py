import json
from pprint import pprint
from sre_constants import RANGE

movie_info_idx = ['id', 'title', 'vote_average', 'overview']
movie_info_dict = {} # 각 영화별 내용을 담는 딕셔너리
movie_info_dict_final = [] # 그 딕셔너리를 추가해 여러 영화의 내용을 담은 리스트 
# 리스트[{영화 딕셔너리1}, {영화 딕셔너리2}, ..., {영화 딕셔너리20}] 


def movie_info(movies_list, genres_list): 

    temp_movie_info_dict = {}

    for i_2 in range(len(movies_list)): # 전체 영화들을 하나씩 할당
        temp_movie_info_dict = movies_list[i_2] # 특정 영화 하나를 임시 딕셔너리에 할당

        for i in range(len(movie_info_idx)):
            for j in temp_movie_info_dict:
                if movie_info_idx[i] == j:
                    movie_info_dict[movie_info_idx[i]] = temp_movie_info_dict.get(j) #04-05번 코드와 동일

    
        temp_dict = {}
        temp_list = []

        for a in range(len(genres_list)):
            temp_dict = genres_list[a] 
       
            if temp_dict['id'] in temp_movie_info_dict['genre_ids']: # id 확인을 통해 코드가 같으면
                temp_list.append(temp_dict["name"]) # 해당 장르 이름을 불러와 새 리스트에 저장
                movie_info_dict["genres_name"] = temp_list 
            # genres_name 이라는 키값에 임시 리스트 내용을 val 값으로 매핑 후 저장 

        movie_info_dict_final.append(movie_info_dict) 
        #각 딕셔너리를 추가해 여러 영화의 내용을 담은 최종 리스트에 추가 
    
    return movie_info_dict_final
         
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))