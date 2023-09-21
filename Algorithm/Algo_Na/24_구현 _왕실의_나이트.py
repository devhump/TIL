# 24. 구현 - 왕실의 나이트
# 내 코드
pos = input()
pos_xy = [int(pos[1]),(ord(pos[0])-96)]
# print(pos_xy)

# dxy = [(-1, -2), (1, -2), (2, -1), (-2,-1),
#        (2, 1), (2, -1), (1, 2), (2, 1)]

cnt = 0 
# 델타값 정의
dx = [-2, -1, 1, 2, 2, 1, -2, -1]
dy = [-1, -2, -2, -1, 1, 2, 1, 2]


result = []
# 델타값을 이용해 이동
for i in range(8):
    x = pos_xy[0]
    y = pos_xy[1]

    nx = x + dx[i]
    ny = y + dy[i]
    
    # 범위를 벗어나지 않으면 갱신
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        x = nx
        y = ny
        cnt += 1

print(cnt)