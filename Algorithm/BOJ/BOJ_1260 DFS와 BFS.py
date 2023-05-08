# BOJ_1260 DFS와 BFS

import sys
sys.stdin = open('BOJ_1260_input.txt', 'r')

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]

def bfs(start, bfs_visited):
    queue = deque([start])
    bfs_visited[start] = True
    bfs_res = [start]
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for adj in graph[v]:
            if not bfs_visited[adj]:
                queue.append(adj)
                bfs_res.append(adj)
                bfs_visited[adj] = True
    return bfs_res

def dfs_re(start, dfs_visited):
    print(start, end=" ")
    dfs_visited[start] = True
    dfs_res.append(start)
    
    for i in graph[start]:
        if not dfs_visited[i]:
            dfs_re(i, dfs_visited)

    return dfs_res

dfs_visited = [False] * (N +1)
bfs_visited = [False] * (N +1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, N+1):
    graph[i].sort()

dfs_res = []
dfs_re(V, dfs_visited)
print()
bfs(V, bfs_visited)
