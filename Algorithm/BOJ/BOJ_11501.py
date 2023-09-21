# BOJ_11501 주식 / 그리디

import sys

sys.stdin = open("BOJ_11501_input.txt", "r")
# import sys

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

# 이제까지 너무 당연하게 range는 앞에서 뒤로만 움직이는 거라 생각했다.
# 답은 나오는데, 왜 계속 시간 초과가 뜰까 했더니, 이런 방법이... 와우...
