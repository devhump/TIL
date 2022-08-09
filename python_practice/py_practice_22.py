# HPHK_문제 21. 무방향 그래프 표현하기

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
    
    
