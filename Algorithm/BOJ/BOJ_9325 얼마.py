# BOJ_9325 얼마?


import sys
sys.stdin = open('BOJ_9325_input.txt', 'r')

for t in range(int(input())):
    res = 0
    res += int(input())
    

    for _ in range(int(input())):
        q, p = map(int, input().split())

        res += (q*p)

    print(res)
