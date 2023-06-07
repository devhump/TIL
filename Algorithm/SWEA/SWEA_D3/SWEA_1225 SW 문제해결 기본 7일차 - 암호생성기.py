# SWEA_1225. [S/W 문제해결 기본] 7일차 - 암호생성기
#1 6 2 2 9 4 1 3 0 
#2 9 7 9 5 4 3 8 0 
#3 8 7 1 6 4 3 5 0 
#4 7 5 8 4 8 1 3 0 
#5 3 8 7 4 4 7 4 0 
#6 6 7 5 9 6 8 5 0 
#7 7 6 8 3 2 5 6 0 
#8 9 2 1 7 3 6 3 0 
#9 4 7 8 1 2 8 4 0 
#10 6 8 9 5 8 5 2 0 

import sys
sys.stdin = open('SWEA_1225_input.txt', 'r')

from collections import deque

T = 10 

for t in range(10):
    N = int(input())
    encode = list(map(int, input().split()))
    queue = deque(encode)

    # print(queue)

    num = 1
    while True: 
        temp = queue.popleft()
        temp -= num
        if temp <= 0:
            queue.append(0)
            break
        queue.append(temp)
        num += 1

        if num > 5:
            num = 1

    print(f"#{t+1}", end=" ")
    print(*queue)