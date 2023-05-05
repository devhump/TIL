
```ad-note
- DFS vs BFS
	- 이론
		- DFS 이론은 👉[[05. 깊이 우선 탐색(DFS)]]
		- BFS 이론은 👉 [[08. DFS & BFS]]
	- 문제 풀이
		- DFS & BFS 기초 문제 풀이 👉 [[09. DFS 와 BFS 기초 문제 풀이]]
		- BFS 문제는 👉 [[BFS & DFS]]
```


![DFS vs BFS](#DFS%20vs%20BFS)


### <문제> BOJ_2178 미로 탐색 : 문제 설명

- [BOJ_2178 미로 탐색](https://www.acmicpc.net/problem/2178)

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

```ad-note
- DFS vs BFS
	- 이론
		- DFS 이론은 👉 [05. 깊이 우선 탐색(DFS)](../KDT/Algorithm/05.%20깊이%20우선%20탐색(DFS).md)
		- BFS 이론은 👉 [08. DFS & BFS](../Algorithm%20(theory)/08.%20DFS%20&%20BFS.md)
	- 문제 풀이
		- DFS & BFS 기초 문제 풀이 👉 [09. DFS 와 BFS 기초 문제 풀이](../Algorithm%20(theory)/09.%20DFS%20와%20BFS%20기초%20문제%20풀이.md)
		- BFS 문제는 👉 [BFS 문제](BFS%20문제.md)
		- DFS 문제는 👉 [DFS 문제](DFS%20문제.md)
```


### <문제> BOJ_2606 바이러스: 문제 설명

- [BOJ_2606 바이러스](https://www.acmicpc.net/problem/2606)

```ad-question
 - 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

- 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

- ![](assets/DFS%20문제.png)

- 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
```

```ad-attention
- 난이도: Silver 3
- 시간제한: ==1초==
- 메모리 제한: ==128MB==

- ==입력== 
	- 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

- ==출력==
	- 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

- ==예제 입력==
	```python
	7
	6
	1 2
	2 3
	1 5
	5 2
	5 6
	4 7
	```
- ==예제 출력==
	```python
	4
	```
```

```python
## 메모리 30840 KB
## 시간 88 ms
## 코드길이 785 B

import sys

com_num = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
# print(com_num, edges)

com_list = [[]*(com_num + 1) for i in range(com_num + 1)]

# 인접 리스트 생성
for i in range(edges):
    v1, v2 = map(int, input().split())
    com_list[v1].append(v2)
    com_list[v2].append(v1)
# pprint(com_list)

# 최초 감염 컴퓨터 리스트
virus_1st = []
virus_1st += com_list[1]

# 연결된 컴퓨터들 확인
virus_final = []
while virus_1st:
    # print(virus_1st)
    temp = virus_1st.pop(0)  

    if temp not in virus_final: # 중복 방지를 위해
        virus_final.append(temp)
        virus_1st += com_list[temp] # 연결된 리스트 연쇄 확인
        # virus_1st = list(set(virus_1st))

print(len(virus_final)-1) # 자기 자신은 제외
```

```python
## 메모리 30840 KB
## 시간 76 ms
## 코드길이 1086 B

import sys

com_num = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
# print(com_num, edges)

com_list = [[]*(com_num + 1) for i in range(com_num + 1)]

# 인접 리스트 생성
for i in range(edges):
    v1, v2 = map(int, input().split())
    com_list[v1].append(v2)
    com_list[v2].append(v1)
# pprint(com_list)

# 최초 감염 컴퓨터 리스트
virus_visited = [False] * (com_num+1)

# print(virus_visited)

virus_1st = []
virus_1st += com_list[1]
virus_visited[1] = True # 자기 자신(1번 컴)을 우선 방문처리

# 연결된 컴퓨터들 확인
while virus_1st:
    # print(virus_1st)
    temp = virus_1st.pop(0)  

    if virus_visited[temp] == True:
        continue
    
    if virus_visited[temp] == False: # 중복 방지를 위해
        virus_visited[temp] = True
        virus_1st += com_list[temp] # 연결된 리스트 연쇄 확인
        virus_1st = list(set(virus_1st)) 
        # set 처리 안 한게 근소하게 더 빠름

# print(virus_visited)
# print(virus_visited.count(True)-1) # 자기 자신은 제외
print(sum(virus_visited)-1)
```

```python
## 메모리 113112 KB
## 시간 116 ms
## 코드길이 563 B

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
```



### <문제> BOJ_11724 연결 요소의 개수: 문제 설명
- [BOJ_11724 연결 요소의 개수](https://www.acmicpc.net/problem/11724)
```ad-question
 - 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
```

```ad-attention
- 난이도: Silver 2
- 시간제한: ==3초==
- 메모리 제한: ==512MB==

- ==입력== 
	- 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

- ==출력==
	- 첫째 줄에 연결 요소의 개수를 출력한다.

- ==예제 입력 1 ==
	```python
	6 5
	1 2
	2 5
	5 1
	3 4
	4 6
	```
- ==예제 출력 1 ==
	```python
	2
	```
- ==예제 입력 2 ==
	```python
	6 8
	1 2
	2 5
	5 1
	3 4
	4 6
	5 4
	2 4
	2 3
	```
- ==예제 출력 2 ==
	```python
	1
	```
```

#### 문제 해결 아이디어
```ad-example
- DFS 문제인 것 같은데 코드 안 보고 1. stack 방식으로 구현 했는데(👏👏👏) 시간 초과가 났고, 2. 재귀 방식으로 변경했더니 recursionError가 떠서 재설정. 다시 돌렸더니 메모리 초과가... ㅠㅠ 결국 남은 건 구글신인가...
	- [백준 RecursionError 해결 안내 페이지](https://help.acmicpc.net/judge/rte/RecursionError)
- 
```

- 시간 초과 코드
```python
# BOJ_11724 연결 요소의 개수
# ! 시간 초과 남

sys.stdin = open('BOJ_11724_input_2.txt', 'r')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (N+1)
visited[0] = True

# print(graph)
# print(visited)


stack = []

def dfs(start):
    visited[start] = True

    stack.append(start)

    cnt1 = 1
    cnt2 = 1
    while cnt1 < N:
        while stack:        
            temp = stack.pop()
            for adj in graph[temp]:
                if not visited[adj]:
                    stack.append(adj)
                    visited[adj] = True
                    # print(visited)
                    cnt1 += 1

        for i in range(len(visited)):
            if visited[i] == False:
                stack.append(i)
                cnt2 += 1
                # print(visited) 
                break

    print(cnt2)

dfs(n1)

```

- 메모리 초과 코드
```python
# BOJ_11724 연결 요소의 개수

import sys
sys.stdin = open('BOJ_11724_input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (N+1)
visited[0] = True

# print(graph)
# print(visited)


stack = []

def dfs(graph, v, visited):
    cnt2 = 1    
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

    for i in range(len(visited)):
        if visited[i] == False:
            stack.append(i)
            cnt2 += 1
            # print(visited) 
            break

    return cnt2

print(dfs(graph, n1, visited))

```

- 통과한 코드
```python
# BOJ_11724 연결 요소의 개수

# sys.stdin = open('BOJ_11724_input.txt', 'r')
# sys.setrecursionlimit(10**6)

# todo 입력 파트
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

# todo DFS 자체는 간결하게
def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# ! dfs 내부에 모든 기능을 넣으려 하지 말고,
# ! 기왕 함수화 시킨거 다른 로직에서 쓰이게만 
# ! 하면 되는 거였다.
cnt = 0
for i in range(1, N+1): # todo 전체 순환하면서 
    if visited[i] == False: # todo 방문하지 않은 경우에는 
    # if not visited[i]:도 가능
        dfs(graph, i, visited) # todo DFS로 연쇄 방문 처리
        cnt += 1 # todo 이 사이클수를 카운팅한다.
        
print(cnt)
```
- 👉 구글링 결과를 확인해 보며 수정한 코드. 기존 stack 방식에서 → 재귀 방식으로 바꿨는데, 틀만 갖다 놨지, 내부 로직이 안 맞았던 거였다. 확실히 이 코드가 더 간단 명료하고 이해하기 쉽구나. 신기한건 구글링 했을 때는 너도나도 다 recursive 제한을 풀어야 돌아가던데, 이건 이 상태로도 가능 하다 👍

- https://ji-gwang.tistory.com/292 → 문제는 통과했지만, 이 코드가 더 정확한 것 같다. 
	- 연결된 그래프가 외 따로 있는 경우도 케어를 해준다. 
- 👇 그리고 아래는 해당 블로그에서 **이 문제를 BFS로 푸는 코드**이다. 
	- 내용은 비슷한데, 다른 블로거가 쓴 코드 → https://soohee410.github.io/coding11
```python
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.

print(count)
```


### <문제> BOJ_4963 섬의 개수: 문제 설명

- [BOJ_4963 섬의 개수](https://www.acmicpc.net/problem/4963)

```ad-question
- 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
- ![](https://www.acmicpc.net/upload/images/island.png)
-  한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
- 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
```

```ad-attention
- 난이도: Silver 2
- 시간제한: ==1초==
- 메모리 제한: ==128MB==

- ==입력== 
	- 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
	- 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
	- 입력의 마지막 줄에는 0이 두 개 주어진다.

- ==출력==
	- 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

- ==예제 입력==
	```python
	1 1
	0
	2 2
	0 1
	1 0
	3 2
	1 1 1
	1 1 1
	5 4
	1 0 1 0 0
	1 0 0 0 0
	1 0 1 0 1
	1 0 0 1 0
	5 4
	1 1 1 0 1
	1 0 1 0 1
	1 0 1 0 1
	1 0 1 1 1
	5 5
	1 0 1 0 1
	0 0 0 0 0
	1 0 1 0 1
	0 0 0 0 0
	1 0 1 0 1
	0 0
	```
- ==예제 출력==
	```python
	0
	1
	1
	3
	1
	9
	```
```

#### 문제 해결 아이디어
```ad-example
- 델타 탐색 문제이면서 DFS 또는 BFS로 푸는 문제라고 생각했다. 
- 매트릭스와 같은 크기의 visited 배열을 설정하고, DFS(또는 BFS)로 매트릭스를 돌면서 방문하지 않은 섬들을 방문 처리를 한다. 
- 섬들로 이루어져있기 때문에 도중에 탐색이 끊길 수 있는데, 이 때 방문하지 않은 좌표를 넣어주면서 그 횟수를 카운팅 하면 된다고 생각한다. 
```


#### 최초 내 코드
```python
# BOJ_4964 섬의 개수

def p_print(list):
        for row in list:
            print(row)

import sys
sys.stdin = open('BOJ_4963_input.txt', 'r')
from collections import deque


# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

while True:

    w, h = map(int, input().split())

    # 종료조건      
    if w == 0 and h == 0:
        break

    island = []

    for i in range(h):
        island.append(list(map(int, input().split())))

    visited = [[False]*w for _ in range(h)]

    cnt = 0 
    for x in range(h):
        for y in range(w):
            cnt += 1
            if visited[x][y] == False:
                queue = deque([(x,y)])

                while queue:
                    x, y = queue.popleft()
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < h and 0 <= ny < w:

                            # if visited[nx][ny] != True: 
                            if island[nx][ny] == 0 :
                                visited = True
                            elif island[nx][ny] == 1:
                                queue.append((nx,ny))

    print(cnt)
```

#### 수정한 코드
```python
# BOJ_4964 섬의 개수
import sys
sys.stdin = open('BOJ_4963_input.txt', 'r')
from collections import deque

def bfs(x, y):
    island[x][y] = 0 
    # !방문한 좌표는 지도에서 0을 지워버리는 식으로 조건을 통과한다.
    queue = deque([(x,y)])
    # * queue = deque()
    # * queue.append([x,y]) 이렇게 많이들 쓰는 듯
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1: # todo 1일 경우(==이동할 수 있는 경우)
                island[nx][ny] = 0 # todo 방문한 좌표는 0으로 처리
                queue.append([nx, ny]) # todo 다음 이동 좌표 큐에 넣기


# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

while True:
    w, h = map(int, input().split())
    # 종료조건      
    if w == 0 and h == 0:
        break

    island = []
    for i in range(h):
        island.append(list(map(int, input().split())))

    visited = [[False]*w for _ in range(h)]

    cnt = 0 
    for x in range(h):
        for y in range(w):
            if island[x][y] == 1:
                bfs(x, y)
                cnt += 1
                
    print(cnt)
```

- DFS로 푸는 코드 👉 [블로그 주소](https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-4963%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
- [ ] 유사한 문제 [BOJ_2667 단지번호붙이기](https://www.acmicpc.net/problem/2667)

### <문제> BOJ_1926 그림: 문제 설명
- [BOJ_1926 그림](https://www.acmicpc.net/problem/1926)
```ad-question
 - 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.
```

```ad-attention
- 난이도: Silver 1
- 시간제한: ==1초==
- 메모리 제한: ==256MB==

- ==입력== 
	- 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

- ==출력==
	- 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

- ==예제 입력==
	```python
	6 5
	1 1 0 1 1
	0 1 1 0 0
	0 0 0 0 0
	1 0 1 1 1
	0 0 1 1 1
	0 0 1 1 1
	```
- ==예제 출력==
	```python
	4
	9
	```
```

#### 문제 해결 아이디어
```ad-example
- 이 문제에서는 4방향 델타 탐색을 사용한다. 
- 1로 연결된 '그림'의 개수와 가장 넓은 그림의 너비를 계산하라고 해서 BFS를 사용해 카운팅을 하고, 해당 함수 내에 최대치를 기록하면 될 거라고 생각헀다. 
```

#### 최초 내 코드 
```python
# BOJ_1926 그림
# ! 테케를 바꿔본 결과, 가장 넓은 그림의 넓이는 구해지는데, 
# ! 1의 개수 구하는 부분이 자꾸 틀렸다. 

def p_print(list):
    for row in list:
        print(row)

import sys
sys.stdin = open('BOJ_1926_input.txt', 'r')

from collections import deque

def bfs(x, y):
    global max_cnt
    global cnt
    queue = deque([(x,y)])    
    cnt = 0
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        cnt += 1
                    if max_cnt < cnt:
                        max_cnt = cnt
                else:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True


# @ 입력 파트
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
cnt2 = 0
max_cnt = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if matrix[i][j] == 1:
                cnt2 += 1
            bfs(i, j)

print(cnt2)
print(max_cnt)
```

#### 수정한 코드 
```python
# BOJ_1926 그림

def p_print(list):
    for row in list:
        print(row)

import sys
sys.stdin = open('BOJ_1926_input.txt', 'r')

from collections import deque

def bfs(x, y):
    queue = deque([(x,y)])    
    matrix[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0 # ! 이게 포인트...
                queue.append((nx,ny))
                cnt += 1 
                # * 여기서 1이 연속된 수치, 
                # *즉 가장 큰 너비의 그림 넓이를 구한다.
    return cnt # ! 포인트2

# @ 입력 파트
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# @ 실행파트
paint = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            paint.append(bfs(i,j)) # * 여기서 매 그림의 넓이를 빈 리스트에 넣는다.

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))


```

- [잘 정리된 블로그](https://lakelouise.tistory.com/72)
- [DFS 풀이된 블로그](https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-1926%EB%B2%88-%EA%B7%B8%EB%A6%BCpython)

```ad-tip
- 매트릭스 확인하면서 0으로 처리하는 건 지난번(BOJ_4963 섬) 에도 풀었는데, 왜 생각이 안 났지 하면서도, 또 return 값을 받아 처리하는 코드는 또 배워간다!
```
