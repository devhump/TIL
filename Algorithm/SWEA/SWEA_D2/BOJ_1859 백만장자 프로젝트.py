# BOJ_1859 백만장자 프로젝트 
# ! 시간 초과

import sys
sys.stdin = open('SWEA_1859_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))

    res = 0
    for i in range(n-1):

        max_profit = 0
        for j in prices[i+1:]:
            if (j- prices[i]) > max_profit:
                max_profit = j - prices[i] 

        res += max_profit

    print(f'#{t} {res}')