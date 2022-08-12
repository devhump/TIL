import sys
# from collections import deque
# import heapq


sys.stdin = open("_Flatten.txt")

# input = sys.stdin.readline

T = 10

for t in range(T):
    total_dump = int(input())
    box_heights = list(map(int, input().split()))
    
    len_box = len(box_heights)

    # print(box_heights)
    box_heights.sort()
    # print(box_heights)
    
    for i in range(total_dump):
        box_heights[len_box-1] -= 1
        box_heights[0] += 1
        box_heights.sort()

    answer = box_heights[len_box-1] - box_heights[0]
    print(f"#{t+1} {answer}")

# 우선 순위 큐를 쓰고 싶었는데, 
# 사용법이 기억이 안 나요ㅠㅠ
# 다행히 pass는 했답니다...