# import sys
# sys.stdin = open("BOJ_8958_input.txt", "r")

# T = int(input())

# for i in range(T):

#     bonus_cnt = 0
#     result = 0
#     OX_quiz = input()

#     for i in range(len(OX_quiz)): #인덱스를 이용해 전후 값 비교하기 용이
        
#         # print(f"{i+1}번째 {result} {bonus_cnt}")

#         if OX_quiz[i] == "O":
#             result += 1
#             if i != 0 and OX_quiz[i-1] == "O":
#                 # index: out of range를 방지하기 위해, 인덱스값 [0] 일때는 pass 
#                 # 바로 직전 인덱스 값[i-1] 체크 
#                 bonus_cnt += 1
#                 result += bonus_cnt
#         else:
#             bonus_cnt = 0

#     print(result)


### 재풀이 22. 10. 05
# 
import sys
sys.stdin = open("BOJ_8958_input.txt", "r")


