# 코드가 깔끔하고 명확하네요 😄
# 다만 평균을 구하는 과정에서 나누는 것이 아니라 몫을 구하셨네요.
# 이번 문제에서는 정답이 되었지만 평균 '미만' 이라는 조건으로 
# 바뀌더라도 코드가 틀릴 수 있습니다.
# 이번 문제에 한해서 괜찮다는 사실을 한 번 더 체크하시면 
# 더욱 큰 발전 할 수 있을 것 같습니다.
# 고생하셨습니다 👍


# SWEA_10505. 소득불균형 #D3

import sys
sys.stdin = open("exam_02_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1

    N = int(input())
    income = list(map(int, input().split()))

    avarage = (sum(income))/N 
    #평균값: 입력받은 값 한번에 더하고, 바로 입력값 개수(사람 수) 만큼 나눠줌 

    cnt = 0 

    for i in range(N):
        if income[i] <= avarage: #평균값보다 적게 버는 수 카운팅
            cnt += 1
    
    print(f"#{case_num} {cnt}")