# BOJ_1302 베스트셀러

import sys
sys.stdin = open("BOJ_1302_input.txt", "r")

cnt = int(input())

best_sell = {}
for i in range(cnt):
    temp = input()
    if best_sell.get(temp, 0):
        best_sell[temp] += 1
    else: 
        best_sell[temp] = 1


max_cnt = 0 
for v in best_sell.values():
    if v >= max_cnt:
        max_cnt = v

most_best = []
for k, v in best_sell.items():
    if v == max_cnt:
        most_best.append(k)

most_best.sort()        

# for i in range(len(most_best)):
print(most_best[0])