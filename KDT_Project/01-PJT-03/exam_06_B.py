# 접근 방식이 정석적인 풀이입니다.
# 코드를 조금씩만 더 다듬는다면 아주 완벽한 풀이가 될 것 같습니다.
# 첫번째로 입력을 받는 단계에서 card_16 = input().replace('-' , '')로 한다면
# '-'가 없는 문자열로 형식을 맞춰줄 수 있습니다.
# 다음으로 if len(card_16)==16 and (card_16[0] in "34569"):
# 이렇게 조건문을 설정한다면 더욱 깔끔하고 직관적인 코드가 될 수 있겠네요
# 풀이가 너무 좋아 디테일한 부분에서 피드백을 남깁니다. 😄

# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.

import sys
sys.stdin = open("exam_06_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1
    card_16 = list(input().replace('-', ''))
    # print(f"{card_16} {len(card_16)}")
    
    # 숫자개수 16되는지 & "34569" 중 하나로 시작하는지 확인
    if len(card_16) == 16 and (card_16[0] in "34569"):
        print(f"#{case_num} {1}")
    else:
        print(f"#{case_num} {0}")