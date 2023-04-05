import sys
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

