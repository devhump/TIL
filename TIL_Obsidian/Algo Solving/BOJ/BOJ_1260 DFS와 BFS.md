---
title : 
aliases : []
tags : [Algorithm/DFS_BFS, ]
---


### <문제> BOJ_1260 DFS와 BFS: 문제 설명
- [BOJ_1260 DFS와 BFS](https://www.acmicpc.net/problem/1260)
```ad-question
 - 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
```

```ad-attention
- 난이도: Silver 2
- 시간제한: ==2초==
- 메모리 제한: ==128MB==

- ==입력== 
	- 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

- ==출력==
	- 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

- ==예제 입력 1==
	```python
	4 5 1
	1 2
	1 3
	1 4
	2 4
	3 4
	```
- ==예제 출력 1==
	```python
	1 2 4 3
	1 2 3 4
	```
- ==예제 입력 2==
	```python
	5 5 3
	5 4
	5 2
	1 2
	3 4
	3 1
	```
- ==예제 출력 2==
	```python
	3 1 2 5 4
	3 1 4 2 5
	```
- ==예제 입력 3==
	```python
	1000 1 1000
	999 1000
	```
- ==예제 출력 3==
	```python
	1000 999
	1000 999
	```

```

#### 문제 해결 아이디어
```ad-example
- 간단한 DFS, BFS 문제라 생각했는데, 답이 안 나와서 찾아보니, '단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고' 라는 조건이 있었다. 
- 그래서 처음에는 bfs/dfs 함수 내부에서 sort 를 해야하나 하고 있었는데, 기존 내 코드에서, 그래프 입력 이후에 sort 한번만 해주면 되는 거였다!
```

#### 최초 내 코드 
```python
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]

def bfs(start, bfs_visited):
    queue = deque([start])
    bfs_visited[start] = True
    bfs_res = [start]
    while queue:
        v = queue.popleft()
        for adj in graph[v]:
            if not bfs_visited[adj]:
                queue.append(adj)
                bfs_res.append(adj)
                bfs_visited[adj] = True
    return bfs_res

def dfs_re(start, dfs_visited):
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

dfs_res = []
ans1 = dfs_re(V, dfs_visited)
ans2 = bfs(V, bfs_visited)

for i in ans1:
    print(i, end=" ")
print()
for i in ans2:
    print(i, end=" ")

```

#### 수정한 코드 
```python
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]

def bfs(start, bfs_visited):
    queue = deque([start])
    bfs_visited[start] = True
    bfs_res = [start]
    while queue:
        v = queue.popleft()
        for adj in graph[v]:
            if not bfs_visited[adj]:
                queue.append(adj)
                bfs_res.append(adj)
                bfs_visited[adj] = True
    return bfs_res

def dfs_re(start, dfs_visited):
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

for i in range(1, N+1): # ! 이 두 줄만 넣으니, 바로 통과!
	graph[i].sort() # ! ... 
- [ ] # graph.sort() 한줄로도 가능

dfs_res = []
ans1 = dfs_re(V, dfs_visited)
ans2 = bfs(V, bfs_visited)

for i in ans1:
    print(i, end=" ")
print()
for i in ans2:
    print(i, end=" ")

```

- [그래프 입력 받은 후 sort를 한 코드 - 블로그](https://velog.io/@gene028/BOJ-1260%EB%B2%88-DFS%EC%99%80-BFS)
- [함수 내에서 정렬해주는 로직의 코드 - 블로그](https://velog.io/@uoayop/BOJ-1260-DFS%EC%99%80-BFSPython)

