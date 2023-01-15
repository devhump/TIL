import sys

input = sys.stdin.readline
total_cnt = int(input())

for i in range(total_cnt):
    cnt = int(input())

    price_list = list(map(int, input().split()))

    result = 0
    max_val = price_list[-1]
    for j in range(cnt - 2, -1, -1):
        if price_list[j] > max_val:
            max_val = price_list[j]
        else:
            result += max_val - price_list[j]

    print(result)