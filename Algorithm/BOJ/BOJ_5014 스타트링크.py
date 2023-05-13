# BOJ_5014 스타트링크 

import sys
sys.stdin = open('BOJ_5014_input.txt', 'r')

from collections import deque

def bfs(n):
    queue = deque([n])

    while queue:

        if S > G and D == 0:
            print("use the stairs")
            break

        x = queue.popleft()

        if x == G:
            print(dist[x])
            break
        elif dist[x] > F:
            print("use the stairs")
            break
        for nx in (x + U, x - D):
            if 0 <= nx <= F and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

F, S, G, U, D = map(int, input().split())


Max_dist = 10**6
dist = [0] * (Max_dist+1)

bfs(S)