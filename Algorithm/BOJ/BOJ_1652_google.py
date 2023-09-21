# BOJ_1652 google

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

ans = [0, 0]
for i in range(n):
    leng_r, leng_c = 0,0
    for j in range(n):
        # 가로
        if board[i][j] == '.':
            leng_r += 1
        else:
            leng_r = 0

        if leng_r == 2:
            ans[0] += 1

        # 세로
        if board[j][i] == '.':
            leng_c += 1
        else:
            leng_c = 0
        
        if leng_c == 2:
            ans[1] += 1

print(*ans)

# todo 내 코드 보다 훨씬 간결하고, 알아보기 쉬운 것 같다.
# todo 일일이 .가 연속되는지 확인하는 것 보다 
# todo 카운터를 사용해서 2개 이상이면 반응하도록.
# https://my-coding-notes.tistory.com/525

# * 또 다른 사람 코드 중에서, 내가 X가 없는 경우 카운팅 하는 문제를 
# * 기존 문자열 마지막에 전부 X를 붙이는 식으로 해결을 한 케이스도 있었다. 
# * 가령, room.append(list(map(str, input())) + ['X'])
# https://alpyrithm.tistory.com/60