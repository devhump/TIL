from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    cnt = 1
    while queue:
        x = queue.popleft()
        cnt += 1
        for adj in graph[x]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)
                ans[adj] = ans[x] + 1

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())

    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n+1)
ans = [0] * (n+1)
bfs(a)

if ans[b] == 0:
    print(-1)
else:
    print(ans[b])
