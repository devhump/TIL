import sys
sys.stdin = open("BOJ_2615_input.txt", "r")

n = 19
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

# 반복문을 통해 바둑알이 있는 위치를 탐색
for x in range(n):
    for y in range(n):
        if board[x][y] != 0:
            focus = board[x][y] # 바둑알의 색

            # 우/아래/대각선 우 아래/ 대각선 우 위 => 4가지 방향을 탐색
            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                # 반복문을 통해 오목이 되는지 확인
                # 해당 좌표가 배열을 벗어나는지와 & 계속 같은 숫자를 가르키는지 확인 
                while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == focus:
                    cnt += 1

                    # 오목이라면
                    if cnt == 5:
                        # todo 육목 체크
                        # ! 바둑돌 5개 맞춘 이전의 돌
                        if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and board[x - dx[i]][y - dy[i]] == focus:
                            break
                        # ! 바둑돌 5개 맞춘 이후의 돌
                        if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and board[nx + dx[i]][ny + dy[i]] == focus:
                            break
                        # 육목이 아니면 성공한거니까
                        # 바둑알의 색과 위치를 출력 후 종료
                        print(focus)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    # 이전에 이동했던 방향으로 다시 이동
                    nx += dx[i]
                    ny += dy[i]

print(0)
