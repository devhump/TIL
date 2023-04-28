- BFS 문제는 👉 [BFS 문제](BFS%20문제.md)

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