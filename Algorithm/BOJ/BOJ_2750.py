#BOJ_2750. 수 정렬하기

###################################################
# 풀이1 - 리스트 이용
#  
# 메모리: 30840KB	시간: 112ms
###################################################


# import sys
# sys.stdin = open("BOJ_2750_input.txt")

# T = int(input())

# num_list = []

# for i in range(T):
#     num = int(input())
#     num_list.append(num)

# num_list = sorted(num_list)

# for i in range(T):
#     print(num_list[i])


###################################################
# 풀이2 - 우선순위 큐 사용
#  
# 메모리: 32908KB	시간: 120ms
###################################################

import sys
import heapq
sys.stdin = open("BOJ_2750_input.txt")

heap = []

T = int(input())

for i in range(T):
    num = int(input())
    heapq.heappush(heap, num)

while heap:
    print(heapq.heappop(heap))
