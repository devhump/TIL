# SWEA_10505. 소득불균형 #D3

import sys
sys.stdin = open("exam_02_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1

    N = int(input())
    income = list(map(int, input().split()))

    avarage = (sum(income))//N 
    #평균값: 입력받은 값 한번에 더하고, 바로 입력값 개수(사람 수) 만큼 나눠줌 

    cnt = 0 

    for i in range(N):
        if income[i] <= avarage: #평균값보다 적게 버는 수 카운팅
            cnt += 1
    
    print(f"#{case_num} {cnt}")