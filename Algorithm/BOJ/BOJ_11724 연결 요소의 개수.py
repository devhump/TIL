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