# # #BOJ_5533. 유니크

# # from pprint import pprint

# import sys
# sys.stdin = open("BOJ_5533_input.txt")

# # M: 가로 행
# N = 3 # 세로 열 고정
# M = int(input())

# card_matrix = [list(map(int, input().split())) for i in range(M)]

# # print(card_matrix)

# score_list = []
# for j in range(3):
#     temp_list = []
#     # A = card_matrix[j][i]
    
#     for i in range(M):
#         temp_list.append(card_matrix[i][j]) 
        
#     score_list.append(temp_list)

# # print(score_list)

# # # 논리 검증 코드
# # # if card_matrix[4][2] in score_list[2]:
# # #     print("yes")
# # # else:
# # #     print("No")

# for i  in range(M):
#     result = 0
#     for j in range(3):
#         print(f"[{i}][{j}] 행렬 값: {card_matrix[i][j]}")
#         print(score_list[j])
#         if score_list[j].count(card_matrix[i][j]) > 1:
#             # print("0 point")
#             result += 0
#         else:
#             result += card_matrix[i][j]
#             # print("got score")    
#     print(result)

#######################################################################
### 제출용 코드 ###
#######################################################################

#BOJ_5533. 유니크


import sys

# M: 가로 행
# N = 3 # 세로 열 고정
M = int(input())

card_matrix = [list(map(int, input().split())) for i in range(M)]

score_list = []
for j in range(3):
    temp_list = []
    
    for i in range(M):
        temp_list.append(card_matrix[i][j]) 
        
    score_list.append(temp_list)

for i  in range(M):
    result = 0
    for j in range(3):

        if score_list[j].count(card_matrix[i][j]) > 1:
            result += 0
        else:
            result += card_matrix[i][j]
    print(result)

