from operator import truediv
import sys

sys.stdin = open("_창용마을무리의개수.txt")

def p_print(list):
    for row in list:
        print(row)


def DFS(start):
    global cnt
    stack = [start]
    visited[start] = True

    while stack:

        start = stack.pop()
        for adj in adj_list[start]:
            if not visited[adj]:
                print(f"adj: {adj}")
                visited[adj] = True
                stack.append(adj)
                cnt += 1


T = int(input())

for t in range(T):

    # N: 노드 수; M: 간선 수
    N, M = map(int, input().split())

    adj_list = [[] for i in range(N+1)]
    # print(adj_list)

    #인접리스트 생성
    for j in range(M):
        v1, v2 = map(int, input().split())
        
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    # p_print(adj_list)

    #방문리스트 생성
    visited = [False] * (N+1)
    # visited[0] = True
    # print(visited)

    cnt = 0
    stack = []
    for i in range(len(adj_list)):
        if len(adj_list[i]) != 0:
            DFS(i)

    # print(visited)
    print(f"#{t+1} {cnt}")
    # cnt를 어디에 걸어야 할지 모르겠다...