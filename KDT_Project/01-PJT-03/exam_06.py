# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.

import sys
sys.stdin = open("exam_06_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1
    card_16 = list(input())

    # print(f"변경전: {card_16} {len(card_16)}")

    del_card_16 = []

    for char in card_16:
        if char != '-':
            del_card_16.append(char)

    # print(f"변경후: {len(del_card_16)}")
    # # print()
    if len(del_card_16) != 16: #숫자개수 16되는지 확인
        print(f"#{case_num} {0}")
    else:
        if del_card_16[0] == "3" or del_card_16[0] == "4" or del_card_16[0] == "5" or del_card_16[0] == "6" or del_card_16[0] == "9":
            print(f"#{case_num} {1}")
        else:
            print(f"#{case_num} {0}")