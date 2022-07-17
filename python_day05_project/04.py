import json
from pprint import pprint

movie_info_idx = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
movie_info_dict = {}

def movie_info(movie):
    
    for i in range(len(movie_info_idx)):        
        for j in movie_json:
            if i in movie_json:
                movie_info_dict[i] = movie_json.get(i)
            
    return movie_info

with open("./data/movie.json", "r", encoding= 'utf-8') as f:
#    movie_json = f.read().split(sep=',') 

    movie_json = json.load(f)
    
    # print(type(movie_json))
    # pprint(movie_json)

    cnt = 0
    cnt_2 = 0
    for i in range(len(movie_info_idx)):
        #print(f"반복문 1 실행 i:{i}  m_i_i[i] {movie_info_idx[i]}")        
        for j in movie_json:

            cnt_2 += 1
            # print(f"j: {j} {cnt_2}번째 반복문 2 실행")
            if movie_info_idx[i] in movie_json:

                cnt += 1
                # print(f"{cnt} 번째 조건문 실행")
                # print(f"movie_json.get(j): {movie_json.get(j)}")
                movie_info_dict[movie_info_idx[i]] = movie_json.get(j)
                pprint((movie_info_dict))   


#################################################################
# 출력값 확인 후 수정요
# 값 덮어쓰기 및 중복 실행 
#################################################################

# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     movie_json = open('data/movie.json', encoding='UTF8')
#     movie = json.load(movie_json)
    
#     pprint(movie_info(movie))