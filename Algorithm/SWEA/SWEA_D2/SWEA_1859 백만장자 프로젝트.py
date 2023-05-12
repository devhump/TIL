# SWEA_1859 백만장자 프로젝트 
# ! 시간 초과

import sys
sys.stdin = open('SWEA_1859_input.txt', 'r')

T = int(input()) # 테스트 케이스

for t in range(1, T+1):
    n = int(input()) # 몇일 동안
    prices = list(map(int, input().split())) # 각 일별 가격

    res = 0
    for i in range(n-1, 0, -1):
        print(prices[i])
        # if prices[i] > prices[i+1]:
        #     max_profit = prices[]


    #     max_profit = 0
    #     for j in prices[i+1:]: # 구매한 다음날 금액 중에서 
    #         if (j- prices[i]) > max_profit: # 차익이 max_profit 보다 크면
    #             max_profit = j - prices[i] # 해당 차익을 max_profit으로 설정

    #     res += max_profit # 이러한 최대 이익을 전부 더한다.

    # print(f'#{t} {res}')

