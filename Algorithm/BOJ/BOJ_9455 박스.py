# BOJ_9455 박스
# ! 왜 또 테케는 맞는데, 틀렸다고 나오냐!!!!!

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
        # todo 1이 (박스가) 없는 경우도 고려
        if 1 not in t_mx[j]:
            break
        one_cnt = t_mx[j].count(1) 
        
        while True:
        
            if one_cnt == sum(t_mx[j][-one_cnt:]):
                break
            # print("변하기 전", t_mx[j])
            for i in range(m-1):
                if t_mx[j][i] == 1 and t_mx[j][i+1] == 0:
                    t_mx[j][i+1] = 1
                    t_mx[j][i] = 0
                    cnt += 1
                    # print("변한 후", t_mx[j])
    print(cnt)
        
