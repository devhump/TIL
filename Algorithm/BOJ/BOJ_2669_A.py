# BOJ_2669. 직사각형 네개의 합집합의 면적 구하기


### 런타임 에러(python3, pypy3)
from pprint import pprint

import sys
sys.stdin = open("BOJ_2669_input.txt")

num = 4

rect_li = []
for i in range(num):
    rect_li.append(list(map(int, input().split())))

temp_list_1 = []
temp_list_2 = []
for i in range(num):
    temp_list_1.append(rect_li[i][0])
    temp_list_1.append(rect_li[i][2])
    temp_list_2.append(rect_li[i][1])
    temp_list_2.append(rect_li[i][3])

N = max(temp_list_1) + 1
M = max(temp_list_2) + 1

# print(M, N)

empty_list = []
for i in range(M):
    empty_list.append([0] * N)

# for row in empty_list:
#     print(row)
# print()

for k in range(num):
    for i in range(rect_li[k][0], rect_li[k][2]):
        for j in range(rect_li[k][1], rect_li[k][3]):
            empty_list[i][j] = 1

# for row in empty_list:
#     print(row)
# print()

result = 0
for row in empty_list:
    result += sum(row)

print(result)
