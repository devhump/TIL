---
title : 
aliases : []
tags : [algorithm/DFS&BFS, ]
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

### <문제> BOJ_2667 단지 번호 붙이기: 문제 설명
- [BOJ_2667 단지 번호 붙이기](https://www.acmicpc.net/problem/2667)
```ad-question
 - <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

- ![](https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png)
```

```ad-attention
- 난이도: Bronze / Silver / Gold
- 시간제한: ==1초==
- 메모리 제한: ==256MB==

- ==입력== 
	- 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

- ==출력==
	- 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

- ==예제 입력==
	```python
	7
	0110100
	0110101
	1110101
	0000111
	0100000
	0111110
	0111000
	```
- ==예제 출력==
	```python
	3
	7
	8
	9
	```
```

#### 문제 해결 아이디어
```ad-example
- 문제 예시에서 나타낸 것 처럼 각 단지별 숫자를 적고, 이걸 카운팅 하는 방식으로 구현을 했다. 근데 테케는 통과하는데 제출에서 걸리네.
- 구글링한 결과 visieted 만들어서 체크하는 방식은 안 된다고 하는데 이유를 모르겠다.
```

#### 최초 내 코드 
```python
# BOJ_2667 단지번호 붙이기
# ! 테케는 통과하는데, 제출하면 틀린다..ㅠㅠ

import sys
sys.stdin = open('BOJ_2667_input.txt', 'r')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    stack = [(x, y)]

    while stack:
        temp = stack.pop()

        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = cnt
                    visited[nx][ny] = True
                    stack.append((nx,ny))
                else:
                    visited[nx][ny] = True
N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input())))

visited = [[False]*N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            dfs(i,j, cnt)

# def p_print(list):
#     for row in list:
#         print(row)

# p_print(matrix)

# [0, 1, 1, 0, 2, 0, 0]
# [0, 1, 1, 0, 2, 0, 2]
# [1, 1, 1, 0, 2, 0, 2]
# [0, 0, 0, 0, 2, 2, 2]
# [0, 3, 0, 0, 0, 0, 0]
# [0, 3, 3, 3, 3, 3, 0]
# [0, 3, 3, 3, 0, 0, 0]

res = []
for i in range(N):
    res.extend(matrix[i]) 
# 각 단지별 숫자가 매핑된 매트릭스를 하나의 리스트로 만들어 준다. 
# [0, 1, 1, 0, 2, 0, 0, 0, 1, 1, 0, 2...]
# print(res)

apt_cnt = max(res) # 이 중에서 가장 큰 값을 찾고, 
ans = []
for i in range(1, apt_cnt+1):
    ans.append(res.count(i)) # 각 단지별 해당하는 가구 수를 센다
ans.sort() # 정렬해서 
print(apt_cnt) #출력 
for i in range(apt_cnt): # 출력2
    print(ans[i])

```

- [참고한 블로그](https://great-park.tistory.com/17)
#### 수정한 코드 
```python
# BOJ_2667 단지번호 붙이기_B (queue)

import sys
sys.stdin = open('BOJ_2667_input.txt', 'r')

from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque([(a, b)])

    matrix[a][b] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft() # @ 이렇게 한번에 뽑기가 가능하군!

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1:
                    queue.append((nx,ny))
                    matrix[nx][ny] = 0
                    cnt += 1
    if cnt != 0:
        ans.append(cnt)
                    
N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

ans = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            bfs(i,j)

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
```


#### 공부해 볼 코드
- [블로그 주소](https://it-sunny-333.tistory.com/32)
```python
from collections import deque, Counter
from functools import reduce

def p_print(list):
    for row in list:
        print(row)

import sys
sys.stdin = open('BOJ_2667_input.txt', 'r')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))
# @ a = [list(map(int,list(input()))) for _ in range(n)]
# @ 이렇게 한 줄로도 입력 가능!

group =[[0]*N for _ in range(N)]

def bfs(a, b, cnt):
    queue = deque([(a, b)])
    group[a][b] = cnt

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1 and group[nx][ny] == 0:
                    queue.append((nx, ny))
                    group[nx][ny] = cnt

cnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)

# p_print(group)
# [0, 1, 1, 0, 2, 0, 0]
# [0, 1, 1, 0, 2, 0, 2]
# [1, 1, 1, 0, 2, 0, 2]
# [0, 0, 0, 0, 2, 2, 2]
# [0, 3, 0, 0, 0, 0, 0]
# [0, 3, 3, 3, 3, 3, 0]
# [0, 3, 3, 3, 0, 0, 0]

print(cnt)
# 각 단지마다 집 개수 출력
# 2차원 배열을 1차원으로 쭈욱 펼치기 
ans = reduce(lambda x,y : x+y, group) 
# [0, 1, 1, 0, 2, 0, 0, 0, 1, 1, 0, 2, 0, 2, 1, 1, 1, 0, 2, 0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 0]

# 단지로 등록?된 집들만 ans 리스트에 남기기
ans = [x for x in ans if x > 0]
# [1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]

# cnt(단지번호) 별 개수(Counter.values()) 구하고 출력
ans = sorted(list(Counter(ans).values()))
# [7, 8, 9]

print('\n'.join(map(str,ans))) # ! 모르는 문법도 아닌데, 이렇게 쓰이니 신구하구만!
```

```ad-tip
- reduce?
	- reduce 함수는 \***반복 가능한** **객체(iterable object)** 내 각 요소를 연산한 뒤 이전 연산 결과들과 누적해서 반환해 주는 함수입니다.
	- [reduce](../Python/Python%20유용한%20문법%20정리.md#reduce) 내용 정리
```

```ad-tip
- Counter?
	- 리스트 내부 요소의 개수를 센다.
	- [Counter](../Python/Python%20유용한%20문법%20정리.md#Counter) 내용 정리
```

#### DFS(재귀) 방식을 활용한 풀이
- [블로그 주소](https://it-sunny-333.tistory.com/32)
```python
n = int(input())
a = [list(map(int, input())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 각 단지마다 집의 개수
cnt = 0
ans = []

# 방문체크용
dist = [[False] * n for _ in range(n)]


def dfs(x, y):
    # 집 개수 증가 & 방문체크
    global cnt
    cnt += 1
    dist[x][y] = True

    # 인접한 노드 탐색하면서 연결되어 있으면 dfs 재귀호출
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1 and dist[nx][ny] == False:
                dfs(nx, ny)



# 모든 정점을 확인해서 시작점이 될 수 있는지 확인. 시작점 가능하면 dfs 탐색 ㄱ
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and dist[i][j] == False:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
print('\n'.join(map(str, ans)))
```