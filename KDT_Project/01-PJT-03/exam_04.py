# 3456. 직사각형 길이 찾기

import sys
sys.stdin = open("exam_04_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1
    a, b, c = map(int, input().split())

    if a == b and a == c:
        print(f"#{case_num} {a}")
    else:
        if a == b:
            print(f"#{case_num} {c}")
        elif b == c:
            print(f"#{case_num} {a}")
        elif c == a:
            print(f"#{case_num} {b}")
