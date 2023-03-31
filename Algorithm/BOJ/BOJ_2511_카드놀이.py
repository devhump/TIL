# BOJ_2511_카드놀이

A_cards = list(map(int, input().split()))
B_cards = list(map(int, input().split()))

score_A = 0
score_B = 0
board = []
for i in range(len(A_cards)):
    temp_A = A_cards.pop(0)
    temp_B = B_cards.pop(0)

    if temp_A > temp_B:
        score_A += 3
        board.append('A')
    elif temp_B > temp_A:
        score_B += 3
        board.append('B')
    else:
        score_A += 1
        score_B += 1
        board.append('D')

if score_A > score_B:
    print(score_A, score_B)
    print("A")
elif score_B > score_A:
    print(score_A, score_B)
    print("B")
elif score_B == score_A:
    if 'A' not in board and 'B' not in board:
        print(score_A, score_B)
        print("D")
    else:
        while True:
            temp = board.pop()
            if temp != "D":
                break

        print(score_A, score_B)
        print(temp)