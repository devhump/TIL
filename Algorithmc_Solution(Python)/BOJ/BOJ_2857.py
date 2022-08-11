# BOJ_2857. FBI

import sys
sys.stdin = open("BOJ_2857_input.txt")

T = 5
cnt = 0
for i in range(T):
    FBI_str = input()

    if "FBI" in FBI_str:
            print(i+1, end=" ")
            cnt += 1

if cnt == 0:
    print("HE GOT AWAY!")
