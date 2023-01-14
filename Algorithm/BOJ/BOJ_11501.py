# BOJ_11501 주식 / 그리디
# 시간초과ㅠㅠ

import sys

sys.stdin = open("BOJ_11501_input.txt", "r")
# import sys

input = sys.stdin.readline
total_cnt = int(input())

for i in range(total_cnt):
    cnt = int(input())

    price_list = list(map(int, input().split()))

    result = 0
    for j in range(cnt - 1):

        max_ = 0
        for num in price_list[j:]:

            if num > max_:
                max_ = num

        if max_ != 0:

            result += max_ - price_list[j]

    print(result)
