fruits_list = []

with open('data/fruits.txt', 'r', encoding= 'utf-8') as f:
    fruits_list = f.read().split(sep='\n')
    # 전체를 읽어오면서 \n 단위로 잘라 리스트에 추가
    fruits_list_abc = sorted(set(fruits_list))
    # 중복된 과일 이름 제거 후, 정렬해서 색인 리스트를 만듦


# # 풀이 1. 두가지 변수 각각 직접 출력
# with open('03.txt', 'w', encoding='utf=8') as f:
#     for name in fruits_list_abc:
#         for i in fruits_list:
#             fruits_list_num = fruits_list.count(name)
         
#         f.write(f"{name} {fruits_list_num}\n")


# 풀이 2. 딕셔너리 활용 (저장 후 출력)
dict_fruit = {}

with open('03.txt', 'w', encoding='utf=8') as f:
    for name in fruits_list_abc: 
        for i in fruits_list:
            fruits_list_num = fruits_list.count(name)
            dict_fruit[name] = fruits_list_num
    
    for i in dict_fruit:
        f.write(f"{i} {dict_fruit[i]}\n")


