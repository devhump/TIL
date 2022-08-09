# HPHK_문제 21. 무방향 그래프 표현하기

import sys

sys.stdin = open("py_practice_22_input.txt")

def pprint(list):
    for row in list:
        print(row)

# N 정점의 개수
# M 간선의 개수
N, M = map(int, input().split())


#Adjacent
Adj_matrix = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    Adj_matrix[v1][v2] = 1

pprint(Adj_matrix)    


Adj_list = [[] for i in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if Adj_matrix[i][j] == 1:
            Adj_list[i].append(j)

print(Adj_list)

