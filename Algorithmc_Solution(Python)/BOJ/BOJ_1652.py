# BOJ_1652. 누울 자리를 찾아라
# 오답 코드

from pprint import pprint

import sys
sys.stdin = open("BOJ_1652_input.txt")

num = int(input())

condo_list = []
for i in range(num):
    condo_list.append(input())

# print(condo_list)
# for row in condo_list:
#     print(row)

cnt_2 = 0
## 가로 행 확인
cnt = 0
row_sum = 0
for i in range(num): #range(len(condo_list)) 와 동일
    cnt_2 += 1
    for j in range(1, num):
        # print(f"i,j=={i},{j}")
        if condo_list[i][j] == "." and condo_list[i][j-1] == ".":
            cnt += 1
            print(f"{cnt_2}번째 실행")
            row_sum += cnt
            break
        else:
            cnt = 0

cnt_2 = 0 
## 세로 열 확인
cnt = 0
col_sum = 0
for j in range(num): #range(len(condo_list)) 와 동일
    for i in range(1, num):
        cnt_2 += 1
        print(f"j,i=={i},{j}")
        if condo_list[i][j] == "." and condo_list[i-1][j] == ".":
            cnt = 1
            print(f"{cnt_2}번째 실행")
            col_sum += cnt
            break

print(row_sum, col_sum)

# # test case 실패
# 5
# XXX.X
# ..XX.
# XX...
# .XX.X
# X....
# 
# >>> 예상 출력 3 2 
# >>> but 실제 : 4 3
