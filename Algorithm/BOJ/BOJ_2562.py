# BOJ_2562 최대값 / 리스트 컴프리헨션

import sys

sys.stdin = open("BOJ_2562_input.txt", "r")

num_list = []
for i in range(9):
    num_list.append(int(input()))

max_ = max(num_list)
print(max_)
print(num_list.index(max_) + 1)

# 리스트 컴프리헨션을 이용한 코드

# data = [int(input()) for _ in range(9)]
# print(max(data))
# print(data.index(max(data))+1)
