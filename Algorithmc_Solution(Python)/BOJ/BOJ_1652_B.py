# BOJ_1652. 누울 자리를 찾아라

## python3, pypy3 둘다 런타임 에러

from pprint import pprint

import sys
sys.stdin = open("BOJ_1652_input.txt")

num = int(input())

condo_list = []
for i in range(num):
    condo_list.append(input())

# for row in condo_list:
#     print(row)

## 가로 행 확인
cnt = 0
row_sum = 0
for i in range(num): #range(len(condo_list)) 와 동일
    for j in range(1, num):
        if condo_list[i][j] == "." and condo_list[i][j-1] == ".":
            cnt = 1
            row_sum += cnt
            break          

## 배열 뒤집은 새로운 배열 설정
reverse_array = []
for i in range(num):
    reverse_array.append([0] * 5)

for i in range(num):
    for j in range(num):
        reverse_array[i][j] = condo_list[j][i]

## 세로 행 확인
cnt = 0
col_sum = 0
for i in range(num): #range(len(condo_list)) 와 동일
    for j in range(1, num):
        if reverse_array[i][j] == "." and reverse_array[i][j-1] == ".":
            cnt = 1
            col_sum += cnt
            break 

print(row_sum, col_sum)         