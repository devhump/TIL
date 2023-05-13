# BOJ_2606 바이러스 


import sys
sys.stdin = open('BOJ_2606_input.txt', 'r')

com = int(input())
graph = [[] for _ in range(com+1)]

for _ in range(int(input())):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) 

visited = [False] * (com+1)
# print(visited)


def dfs(start):
    cnt = 0
    stack = [start]
    visited[start] = True

    while stack:
        # print(f'stack: {stack}')
        
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
                cnt += 1

    print(cnt)

dfs(1)