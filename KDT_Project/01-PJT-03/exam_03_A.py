# SWEA_10804.문자열의 거울상 #D3

import sys
sys.stdin = open("exam_03_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1
    str_list = input()
    # print(str_list, len(str_list), type(str_list))

    mirror_result = '' # 비어있는 문자열 생성

    for i in range(len(str_list)): #알파벳만 교체해줌

        if str_list[i] == "b":
            mirror_result += "d"
        elif str_list[i] == "d":
            mirror_result += "b"
        elif str_list[i] == "p":
            mirror_result += "q" 
        elif str_list[i] == "q":    
            mirror_result += "p"

    print(f"#{case_num} {mirror_result[::-1]}") # 저장된 순서 반대로 출력




# 리스트를 활용하려다 번거로워서 선회
#
# import sys
# sys.stdin = open("exam_03_input.txt")

# T = int(input())
# case_num = 0

# for i in range(T):

#     str_list = input()
#     # print(str_list, len(str_list), type(str_list))

#     mirror_list = []

#     for i in range(len(str_list)):

#         if str_list[i] == "b":
#             mirror_list.append("d")
#         elif str_list[i] == "d":
#             mirror_list.append("b")
#         elif str_list[i] == "p":
#             mirror_list.append("q") 
#         elif str_list[i] == "q":    
#             mirror_list.append("p")

#     print(str_list)
#     print(mirror_list)

    # result = '' 
    # for j in range(len(mirror_list)):
    #     result += mirror_list[-j]
    
    # print(result)

    # print(mirror_list)
    # print(mirror_list[::-1])

