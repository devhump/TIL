M, n = map(int, input().split())

# dxy = {
#     "down": (1, 0),
#     "up": (-1, 0),
#     "right": (0, 1),
#     "left": (0, -1)
# }

# dxy_al = ["up", "right", "down", "left"]
dxy_mat = [(-1, 0), (0, 1), (1, 0), (0,-1)]
dxy_idx = 2
x, y = 0, 0
check = True

for _ in range(n):
    cmd, cnt = input().split()

    if check == False:
        break

    if cmd == "TURN":
        if int(cnt) == 0:
            dxy_idx += -1
        elif int(cnt) == 1:
            dxy_idx -= -1

        if dxy_idx < 0: 
            dxy_idx += 4
        elif 4 <= dxy_idx:
            dxy_idx %= 4
    elif cmd == "MOVE":
        for i in range(int(cnt)):
            
            nx = x + dxy_mat[dxy_idx][0]
            ny = y + dxy_mat[dxy_idx][1]

            if 0 <= nx <= M and 0 <= ny < M:
                x = nx
                y = ny
            else:
                check = False
                break        
    
if check:
    print(x, y)
else:
    print(-1)