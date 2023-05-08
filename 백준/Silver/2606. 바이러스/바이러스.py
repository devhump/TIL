com = int(input())
edges_num = int(input())


graph = [[] for _ in range(com+1)]
for _ in range(edges_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

visited = [False] * (com+1)
def dfs(start):
    visited[start] = True
    stack = [start]
    cnt = 0
    while stack:
        temp = stack.pop()
        for adj in graph[temp]:
            if not visited[adj]:
                cnt += 1
                visited[adj] = True
                stack.append(adj)
    print(cnt)

dfs(1)