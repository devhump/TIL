# BOJ_2669. 직사각형 네개의 합집합의 면적 구하기


### 런타임 에러(python3, pypy3)
from pprint import pprint

import sys
sys.stdin = open("BOJ_2669_input.txt")

num = 4

rectangles_list = []
for i in range(num):
    rectangles_list.append(list(map(int, input().split())))

    

temp_list_1 = []
temp_list_2 = []
for i in range(num):
   temp_list_1.append(rectangles_list[i][0])
   temp_list_1.append(rectangles_list[i][2])
   temp_list_2.append(rectangles_list[i][1])
   temp_list_2.append(rectangles_list[i][3])

N = max(temp_list_1) + 1
M = max(temp_list_2) + 1

# print(M, N)

empty_list = []
for i in range(M):
    empty_list.append([0] * N)

for row in empty_list:
    print(row)
print()

for k in range(num):
    for i in range(rectangles_list[k][0], rectangles_list[k][2]):
        for j in range(rectangles_list[k][1], rectangles_list[k][3]):
            empty_list[i][j] = 1

for row in empty_list:
    print(row)
print()

result = 0
for row in empty_list:
    result += sum(row)

print(result)
