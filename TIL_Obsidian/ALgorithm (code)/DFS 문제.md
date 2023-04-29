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

![DFS vs BFS](BFS%20문제.md#DFS%20vs%20BFS)


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