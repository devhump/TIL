# BOJ_2798. 블랙잭

import sys
sys.stdin = open("BOJ_2798.txt")

# N: 카드 장수
# M: 목표 수
N, M = map(int, input().split())

cards = list(map(int, input().split()))

# result_combi = []
max_sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            # print(i, j, k)
            # print(cards[i], cards[j], cards[k])
            result = cards[i] + cards[j] + cards[k]
            
            if result > max_sum and result <= M:  
                max_sum = result
                # result_combi.append((cards[i],cards[j],cards[k], result))
            if max_sum == M:
                break
        if max_sum == M:
                break
    if max_sum == M:
                break
                
# print(result_combi)
print(max_sum)