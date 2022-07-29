# SWEA_10505

import sys
sys.stdin = open("exam_02_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1

    N = int(input())
    income = list(map(int, input().split()))

    avarage = (sum(income))//N

    cnt = 0 

    for i in range(N):
        if income[i] <= avarage:
            cnt += 1
    
    print(f"#{case_num} {cnt}")