from collections import deque

def bfs(n, check):
    queue = deque([n])
    while queue:

        x = queue.popleft()

        if x == G:
            return visited[x]
        for nx in (x + U, x - D):
            if 0 < nx <= F and not visited[nx] and (nx != S):
                visited[nx] = visited[x] + 1
                queue.append(nx)
    return -1

F, S, G, U, D = map(int, input().split())

visited = [0] *(F+1)
check = False 

ans = bfs(S, check)

if ans >= 0:
	print(ans)
else:
	print("use the stairs")
        
# print(visited)