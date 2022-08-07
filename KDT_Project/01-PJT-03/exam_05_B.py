# range도 너무 잘 활용하였네요 너무 좋습니다.
# 다만 마지막 while 문 대신에 
# result = result % 10 (10으로 나눈 나머지) 로 바꾸고
# result가 0인 경우를 따로 처리하는 코드가 개인적으로는 
# 조금 더 깔끔할 것 같습니다!

# 한번 참고해보시고 비교하시면 좋을 것 같습니다
# 잘하셨습니다 😄


# 14649. 신용카드 만들기 1

import sys
sys.stdin = open("exam_05_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1
    card_15 = list(map(int, input().split()))

    result = 0

    for i in range(0, 15, 2):
        result += (card_15[i] * 2)

    for i in range(1, 15, 2):
        result += card_15[i]

    result = result % 10
    
    if result == 0:
        result = 10

    print(f"#{case_num} {10 - result}")