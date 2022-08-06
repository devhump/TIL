# SWEA_1204.최빈수구하기 #D2

# 코드가 아주 정확하고 명확하네요 ڒڑڐ
# 다만 dict_scores 초기화를 0 부터 100 까지 모두 하시는 과정에서
# 굳이 딕셔너리를 사용하실 필요가 있었을까 하는 생각이 드네요. 차라리 리스트로
# [0]*101 처럼 초기화를 하셨다면
# 최대값을 찾는 과정도 max()를 활용하여 쉽게 계산하실 수 있을 텐데 하는 아쉬움이
# 듭니다.
# 다음에 비슷한 유형에서는 리스트를 활용해 보는 것도 좋은 방법일 것 같네요!


import sys
from pprint import pprint

sys.stdin = open("exam_01_input.txt")

T = int(input())


for i in range(T):
    case_num = int(input())
    scores = list(map(int, input().split()))

    scores_list = []

    for i in range(101): # 0으로 초기화된 리스트 생성
        scores_list.append(0)

    for i in range(0, 100): # 리스트 돌면서 숫자 카운팅
        scores_list[i] = scores.count(i)

    # print(scores_list)
    max_score = max(scores_list)
    idx = scores_list.index(max_score)

    print(f"#{case_num} {idx}") # 최빈값 출력 
