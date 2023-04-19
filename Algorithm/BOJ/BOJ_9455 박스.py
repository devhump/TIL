# BOJ_9455 박스

import sys
sys.stdin = open("BOJ_9455_input.txt", "r")

# import sys 
# input = sys.stdin.readline

from pprint import pprint


T = int(input())

for t in range(T):
    # todo 입력 부분
    mn = list(map(int, input().split()))
    m = mn[0]
    n = mn[1]

    matrix = [[] for _ in range(m)]
    for i in range(m):
        matrix[i].extend(list(map(int, input().split())))

    # pprint(matrix)

    # todo 리스트 회전하는 부분
    t_mx = [[0]* m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            t_mx[i][j] = matrix[j][i]


    # pprint(t_mx)
    cnt = 0
    for j in range(n):
        check = False 
        k = 0
        # todo 1이 (박스가) 없는 경우도 고려
        if 1 not in matrix[j]:
            break
        one_cnt = matrix[j].count(1) 
        
        while one_cnt != sum(matrix[i][one_cnt:]):
            
            for i in range(m-1):
                if matrix[j][i] == 1 and matrix[j][i+1] == 0:
                    matrix[j][i+1] == 1 and matrix[j][i] == 0
                    cnt += 1
        print(cnt)
        
