# BOJ_2644 촌수계산 (BFS 아마도?)

import sys
sys.stdin = open('BOJ_2644_input.txt', 'r')

from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # todo 부모노드가 갖는 노드에 1을 더하는 계산
                res[i] = res[v] + 1 # todo 이게 포인트 구나 
                visited[i] = True

num = int(input())
a,b = map(int, input().split())

graph = [[] for _ in range(num+1)]
for _ in range(int(input())):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (num+1)
res = [0] * (num+1) # todo 여기서 촌수 리스트를 만들면서 0으로 초기화 

bfs(a)

# print(res)

if res[b] > 0:
    print(res[b])
else:
    print(-1)