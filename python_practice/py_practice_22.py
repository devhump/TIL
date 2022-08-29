# HPHK_문제 22. 무방향 그래프 표현하기
# > 그래프 입력이 주어질 때 `무방향` 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 `정점의 개수 N`과 `간선의 개수 M`이 주어진다.  둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.
# >
# ### input
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# ### output
# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0, 1, 0],
#  [0, 1, 0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 1, 0, 0, 1],
#  [0, 1, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0]]
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

import sys

sys.stdin = open("py_practice_22_input.txt")

def pprint(list):
    for row in list:
        print(row)

N, M = map(int, input().split())

graph_list = []
for i in range(M):
    graph_list.append(list(map(int, input().split())))

# pprint(graph_list)

# len(set(*graph_list))
graph_array = [[0]*(N+1) for i in range(N+1)]

for row in graph_list:
    graph_array[row[0]][row[1]] = 1
    graph_array[row[1]][row[0]] = 1

# pprint(graph_array)


vertex_list = [[] for i in range(N+1)]

# print(vertex_list)

for i in range(N+1):
    for g_row in graph_list: 
        if i == g_row[0]:
            vertex_list[i].append(g_row[1])
        
        if i == g_row[1]:
            vertex_list[i].append(g_row[0])


pprint(vertex_list)
    
    
