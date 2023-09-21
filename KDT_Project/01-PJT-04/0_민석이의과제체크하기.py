#SWEA_5431. 민석이의 과제 체크하기 #D3

import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

case_num = 0
for i in range(T):
    report_list = []
    case_num += 1
    N, K = map(int, input().split())
    report_list = list(map(int, input().split()))

    # print(report_list)

    not_report = []
    for i in range(1, N+1):
        if i not in report_list:
            not_report.append(i)
    
    # print(not_report)
    print(f"#{case_num}", end=' ')
    for i in range(N-K):
        print(f"{not_report[i]}", end=' ')
    print()

