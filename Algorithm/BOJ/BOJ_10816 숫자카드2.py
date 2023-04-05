# BOJ_10816 숫자카드2
# * 리스트 반복문 돌리니 계속 시간 초과 떠서 
# * 혹시나 해서 딕셔너리로 돌리니까 통과함.

import sys
sys.stdin = open("BOJ_10816_input.txt", "r")
input = sys.stdin.readline

N = int(input())
sg_cards = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

sg_dict = {}
for i in range(N):
    if sg_dict.get(sg_cards[i], 0) != 0:
        sg_dict[sg_cards[i]] += 1
    else:
        sg_dict[sg_cards[i]] = 1

for j in range(M):
    print(sg_dict.get(cards[j], 0), end=" ")

# card_cnt = [ 0 for _ in range(M)]

## ! 시간 초과 
# for j in range(M):
#     print(sg_cards.count(cards[j]), end=" ")

## ! 시간 초과 
# for i in range(N):
#     for j in range(M):
#         if sg_cards[i] == cards[j]:
#             card_cnt[j] += 1

# for k in range(M):
#     print(card_cnt[k], end=" ") 

