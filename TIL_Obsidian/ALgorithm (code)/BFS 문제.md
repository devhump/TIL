
```ad-note
- DFS vs BFS
	- 이론
		- DFS 이론은 👉[[05. 깊이 우선 탐색(DFS)]]
		- BFS 이론은 👉 [[08. DFS & BFS]]
	- 문제 풀이
		- DFS & BFS 기초 문제 풀이 👉 [[09. DFS 와 BFS 기초 문제 풀이]]
		- BFS 문제는 👉 [[BFS 문제]]
		- DFS 문제는 👉 [[DFS 문제]]
```


![DFS vs BFS](#DFS%20vs%20BFS)

- [BOJ_2178 미로 탐색](https://www.acmicpc.net/problem/2178)

### <문제> BOJ_2178 미로 탐색 : 문제 설명
```ad-question
 - N×M크기의 배열로 표현되는 미로가 있다.
![](assets/BFS%20문제.png)
 - 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

- 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
```

```ad-attention
- 난이도: Silver 1
- 시간제한: ==1초==
- 메모리 제한: ==198MB==

- ==입력== 
	- 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 **붙어서** 입력으로 주어진다.

- ==출력==
	- 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

- ==예제 입력 1==
	```python
	4 6
	101111
	101010
	101011
	111011
	```
- ==예제 출력 1==
	```python
	15
	```
- ==예제 입력 2==
	```python
	4 6
	110110
	110110
	111111
	111101
	```
- ==예제 출력 2==
	```python
	9
	```
- ==예제 입력 3==
	```python
	2 25
	1011101110111011101110111
	1110111011101110111011101
	```
- ==예제 출력 3==
	```python
	38
	```
- ==예제 입력 4==
	```python
	7 7
	1011111
	1110001
	1000001
	1000001
	1000001
	1000001
	1111111
	```
- ==예제 출력 4==
	```python
	13
	```
```

#### 문제 해결 아이디어
```ad-example
- 전부터 미로 탐색 문제를 BFS로 푼다는 얘기는 들었는데, 도저히 어떻게 풀어 나가야 할지 감이 안 잡혔다. 그래서 조금 고민하다가 바로 구글링.
```

#### DFS vs BFS
```ad-tip
**DFS가 유리한 경우**  
- 재귀적인 특징과 백트래킹을 이용하여 모든 경우를 하나씩 전부 탐색하는 경우  
- Graph의 크기가 클 경우  
- Optimal한 답을 찾는 것이 아닌 경우  
- 경로의 특징을 저장해야 하는 경우 ex) 경로의 가중치, 이동 과정에서의 제약  
  
**BFS가 유리한 경우**  
- 최단 거리 or 최단 횟수 구하는 경우  
- Optimal(최적의)한 답을 찾는 경우, BFS는 가장 처음 발견되는 해답이 최단 거리이다!  
- 탐색의 횟수를 구해야 하는 경우(7576번 토마토 문제)
```

- 설명이 아주 자세한 블로그 
	- 👉 https://great-park.tistory.com/m/46

- 나는 델타 탐색에서 nx, ny 할때의 **n이 next**를 의미하는지 오늘 처음 알았다;;

#### 구글링한 코드
```python
# BOJ_2178 미로 탐색 

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

#sys.stdin = open('BOJ_2178_input.txt', 'r')

graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

queue = deque([(0,0)])

# 우 좌 하 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

# BFS
while queue:
    x, y = queue.popleft()
	
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M: # 범위 확인
            if graph[nx][ny] == 1: # 경로 확인
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 # value 자체를 이동 횟수로 사용

print(graph[N-1][M-1])


```


- 그리고 위 코드를 함수화 해서 [해결한 코드](https://yuna0125.tistory.com/61) 👇
```python
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip()))) # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):
    
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

print(bfs(0,0))
```


![](assets/code%20(1).png)


### <문제> BOJ_2644 촌수계산 : 문제 설명
- [BOJ_2644 촌수계산 ](https://www.acmicpc.net/problem/2644)
```ad-question
 - 우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

- 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
```

```ad-attention
- 난이도: Bronze / Silver / Gold
- 시간제한: ==1초==
- 메모리 제한: ==256MB==

- ==입력== 
	- 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

- 각 사람의 부모는 최대 한 명만 주어진다.

- ==출력==
	- 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

- ==예제 입력 1 ==
	```python
	9
	7 3
	7
	1 2
	1 3
	2 7
	2 8
	2 9
	4 5
	4 6
	```
- ==예제 출력 1 ==
	```python
	3
	```
- ==예제 입력 2 ==
	```python
	9
	8 6
	7
	1 2
	1 3
	2 7
	2 8
	2 9
	4 5
	4 6
	```
- ==예제 출력 2 ==
	```python
	-1
	```
```

#### 문제 해결 아이디어
```ad-example
- 최단거리니까 BFS가 아닐까? BFS는 어떻게 구현하더라? 값은 어떻게 넘기지? 카운팅은 어디서 해야할까? - 하는 일련의 과정이 만든 코드. 
- visited는 항상 `[False] * (n+1)`이라고만 생각했는데, 그건 또 아니더라. 하나 배워간다.
```

#### 최초 내 코드
```python
# BOJ_2644 촌수계산 (BFS 아마도?)

import sys
sys.stdin = open('BOJ_2644_input.txt', 'r')

from collections import deque


def bfs(graph, start, visited, check, cnt):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        cnt += 1
        
        if b in queue:
            check = True
            break
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return (check, cnt)

num = int(input())
a,b = map(int, input().split())

graph = [[] for _ in range(num+1)]
for _ in range(int(input())):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


visited = [False] * (num+1)

cnt = 0
check = False
result = bfs(graph, a, visited, check, cnt)


if result[0] == True:
    print(result[1]-1)
else:
    print(-1)
```


#### 수정한 코드
```python
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
```

```ad-hint
1. 촌수를 저장할 리스트를 만들고,
2. bfs 돌리면서 부모노드 촌수 + 1을 해주면
3. 시작점으로 부터 각 노드의 촌수가 나온다.
```

- 그리고 조금씩 다른 코드를 찾았는데, 

1. visited / result 리스트를 따로 나누지 않은 경우 [블로그 주소](https://recordofwonseok.tistory.com/380)
```python
import sys
from collections import deque
input = sys.stdin.readline

def bfs(curr_node):
    queue = deque()
    queue.append(curr_node)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                queue.append(i)


N = int(input())
target_start, target_end = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[target_start] = 0
bfs(target_start)
print(visited[target_end])
```

2. dfs 재귀 횟수를 카운트를 하는 경우 [블로그 주소](https://wonyoung2257.tistory.com/56)
```python
# 입력값 받는 부분
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []
####

# 어떤 노드들이 연결되어 있는지 graph라는 2차원 배열에 저장
for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

# dfs
def dfs(v, num):
  num += 1
  visited[v] = True

  if v == B:
    result.append(num)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)

dfs(A, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)
```

3. DFS를 활용해 해결한 경우 [블로그 주소](https://lbdiaryl.tistory.com/212?category=1010228)
```python
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)

n=int(input())
A,B=map(int,input().split())
m=int(input())

graph=[[] for _ in range(n+1)]
visited = [False] * (n + 1)
res=[0]*(n+1)


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(A)

if res[B]>0:
    print(res[B])
else:
    print(-1)
```