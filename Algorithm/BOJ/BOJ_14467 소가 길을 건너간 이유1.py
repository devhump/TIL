# BOJ_14467 소가 길을 건너간 이유1

import sys
sys.stdin = open('BOJ_14467_input.txt', 'r')

cow_check = [2] * 11 ## 처음 시작은 2로 초기화 하고
cnt = 0
for _ in range(int(input())):
    cow, road = map(int, input().split()) ## 관측 결과를 매번 확인하는데
    
    if cow_check[cow] != road: ## 관측 결과가 바뀌면 체크
        if cow_check[cow] == 2: ## 단, 최초 관측이면(초기화값==2) 그냥 변경
            cow_check[cow] = road
        else:
            cow_check[cow] = road ## 그렇지 않다면 변경하면서
            cnt += 1 # 카운트 +1

# print(cow_check)
print(cnt)