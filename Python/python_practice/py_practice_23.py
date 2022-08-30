# HPHK_문제 23. 유방향 그래프 표현하기
# > 그래프 입력이 주어질 때 `유방향` 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 `정점의 개수 N`과 `간선의 개수 M`이 주어진다.  둘째 줄부터 M개의 줄에 간선의 시작점 u와 끝점 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.
# >

### input 동일
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# ##### output
# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0]]
# [[], [2], [5], [4], [6], [1], []]

import sys

sys.stdin = open("py_practice_23_input.txt")

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

