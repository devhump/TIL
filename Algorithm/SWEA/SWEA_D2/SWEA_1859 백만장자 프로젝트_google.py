# SWEA_1859 백만장자 프로젝트_google

import sys
sys.stdin = open('SWEA_1859_input.txt', 'r')


T = int(input()) # 전체 TC 갯수
for t in range(T): # TC마다
    M = int(input()) #배열의 길이 (안쓰임)
    answer = 0 #출력할 정답
    arr = list(map(int, input().split())) #배열 입력 받기
    sellPrice = 0 #현재 판매가격(최댓값)

    for val in arr[::-1]: # 배열 거꾸로 순회
        if val >= sellPrice: #현재 값이 최댓값보다 크거나 같다면
            sellPrice = val # 최댓값 업데이트
        else:
            answer += sellPrice - val #아니라면 정답값에 가격차이를 더한다. (현재 값에 구매해서 최댓값에 판다)
    print(f"#{t+1} {answer}")