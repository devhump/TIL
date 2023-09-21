# SWEA_1983 조교의 성적 매기기


import sys
sys.stdin = open('SWEA_1983_input.txt', 'r')

import math
T = int(input())

for t in range(T):
    N, K = map(int, input().split())

    score = []
    for _ in range(N):
        mid, fin, task = map(int, input().split())
        score.append(mid*35 + fin*45 + task*20)

    student_score = score[K-1]

    score.sort(reverse=True)

    rank = score.index(student_score)
    # print(len(score), rank)

    res = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    student_num = len(score)
    if student_num > 10:
        div = student_num / 10

        rank = math.floor(rank/div) # todo 이게 조금 헷갈렸다; 
        # todo ceil을 해야하나, floor를 해야하나.

    print(f'#{t+1} {res[rank]}')

