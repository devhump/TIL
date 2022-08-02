# BOJ_11286. 절대값 힙

import sys
import heapq
sys.stdin = open("BOJ_11286_input.txt")

## 시간 초과 
heap = []

T = int(input())

for i in range(T):
    # num = int(input()) #시간초과
    num = int(sys.stdin.readline())

    # print(f"heap:{heap}")

    if num != 0:
        heapq.heappush(heap, (abs(num), num)) # 튜플로도 입력이 가능 앞선 수'abs(num)'를 기준으로 정렬
    elif num == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap)[1]) # 출력을 튜플 구조에서 두번째 인수 출력
                                           # heap:[(1, -1), (1, 1)]
                                           # 이때 최초값은 절대값(abs(num)), 두번째 값은 원래 값(original)