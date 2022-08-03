# BOJ_1236. 성 지키기 

import sys
sys.stdin = open("BOJ_1236_input.txt")

# M: 가로 행
# N: 세로 열
M, N = map(int, input().split())

idx_list = [ ]

for i in range(N):
    idx_list.append(0)
# 인덱스 리스트 [0,0,0,0,0] 설정+

cnt = 0
for i in range(M):

    temp_list = sys.stdin.readline()

    for j in range(N):
        if temp_list[j] == "X": 
            idx_list[j] += 1    #각 자릿수(인덱스별)에 몇개의 X가 있는지 카운팅
                                #각 세로줄별로 X가 없는지 확인 

    if "X" not in temp_list: # 각 가로줄별로 X가 있는지 확인
        cnt += 1             # 없는 줄은 줄 수 카운팅

print(max(idx_list.count(0),cnt)) 
# 두개의 지표(인덱스 vs cnt) 중 작은 수 확인

print(idx_list)
# print(cnt)