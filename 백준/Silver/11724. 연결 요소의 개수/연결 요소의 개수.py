
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (N+1)
# visited[0] = True

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0
for i in range(1, N+1):
    if visited[i] == False:
        dfs(graph, i, visited)
        cnt += 1
        
print(cnt)