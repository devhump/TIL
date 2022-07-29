# SWEA_1204

import sys
from pprint import pprint

sys.stdin = open("exam_01_input.txt")

T = int(input())


for i in range(T):
    case_num = int(input())
    scores = list(map(int, input().split()))

    # print(scores)

    dict_scores = {}

    for i in range(0, 101): # 키값이 0 ~ 100인 빈 딕셔너리 생성
        dict_scores[i] = 0

    # sum_human = 0

    for i in range(0, 101): # 딕셔너리 돌면서 숫자 카운팅
        dict_scores[i] = scores.count(i)
        # sum_human += dict_scores[i] # 검증 코드
    # print(sum_human)

    # pprint(dict_scores)

    max_score = 0
    cnt = 0 

    for i in range(0, 101): # 0 ~ 100 순회 하면서
        if max_score <= dict_scores[i]: # 각 키값에 저장된 val 값 비교
            max_score = dict_scores[i] # 최고값 갱신하며 저장
            # max_score = i 
            # # 처음에 이렇게 짬... 얕은 복사 - 깊은 복사에 대한 이해 부족


    for i in range(0, 101): # 0 ~ 100 순회 하면서
        if max_score == dict_scores[i]: # 각 키값에 저장된 val 값 비교
            temp = i 

    print(f"#{case_num} {temp}") # 최빈값 출력 
