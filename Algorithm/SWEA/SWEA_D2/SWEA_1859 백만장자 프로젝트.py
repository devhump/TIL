# SWEA_1859 백만장자 프로젝트 
# ! 시간 초과

import sys
sys.stdin = open('SWEA_1859_input.txt', 'r')

T = int(input()) # 테스트 케이스

for t in range(1, T+1):
    n = int(input()) # 몇일 동안
    prices = list(map(int, input().split())) # 각 일별 가격

    res = 0
    max_profit = 0
    max_prices = prices[-1] # 최초에는 최대값을 마지막날 가격으로 초기화
    for i in range(n-1, -1, -1):
        if prices[i] > max_prices: # 중간에 더 비싼 금액이 있다면 
            max_prices = prices[i] # 해당 값으로 변경
            continue # 값이 갱신된 회차는 넘어감

        temp = max_prices - prices[i] # 매일의 날짜를 비교해 수익률을 확인 
        
        if max_profit < temp: # 수익률이 더 난다면 
            max_profit = temp  # 해당 값을 최대 수익으로 

        res += max_profit # 최대 수익값 누적합
    print(f'#{t} {res}')


# # ! 시간 초과
# T = int(input())

# for t in range(1, T+1):
#     n = int(input())
#     prices = list(map(int, input().split()))

#     res = 0
#     for i in range(n-1):

#         max_profit = 0
#         for j in prices[i+1:]: # 구매한 날의 다음날들 중에
#             if (j- prices[i]) > max_profit: # 차익을 계산해 보고,
#                 max_profit = j - prices[i]  # 0 이상의 수익이 나면 해당 값을 저장

#         res += max_profit # 최대 수익의 누적합

#     print(f'#{t} {res}')