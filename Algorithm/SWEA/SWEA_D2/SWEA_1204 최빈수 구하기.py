# SWEA_1204 최빈수 구하기

import sys
sys.stdin = open('SWEA_1204_input.txt', 'r')

T = int(input())

for _ in range(T):
    tc = int(input())
    nums = list(map(int, input().split()))

    num_dict = {}
    for num in nums:
        if num_dict.get(num, 0):
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    max_cnt = 0
    res = ""
    for k, v in num_dict.items():
        if max_cnt < v:
            max_cnt = v
            res = k 

    print(f'#{tc} {res}')

