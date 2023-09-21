# BOJ_1697 숨바꼭질

from collections import deque

def bfs(n):
    queue = deque([n])

    while queue:
        x = queue.popleft() # 처음 시작점은 x = 5, q = deque([])
        print(f'x == {x}')
        if x == K:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2): # nx = 4, 6, 10
            if 0 <= nx <= Max_dist and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)  # q = deque([4, 6, "10"])

Max_dist = 10 ** 5
dist = [0] * (Max_dist + 1)
# N, K = map(int, input().split())
N, K = 5, 17

bfs(N)

print(dist[:41])

