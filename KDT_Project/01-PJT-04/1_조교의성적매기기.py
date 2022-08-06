#SWEA_1983. 조교의 성적 매기기#D2

from ast import Num
import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

case_num = 0
for i in range(T):
    case_num += 1
    #전체 학생 수 M와 K번째 학생
    N, K = map(int, input().split())

    #해당 회차 성적 입력 받고
    score_list = []
    for j in range(N):
        score_list.append(list(map(int, input().split())))

    # print(score_list)

    total_score = []
    for i in range(N):
    
        result = 0
        result += (score_list[i][0]*35) # 중간고사
        result += (score_list[i][1]*45) # 기말고사
        result += (score_list[i][2]*20) # 과제
        total_score.append(result)

    # 해당 순서의 학생의 점수 체크
    std_score = total_score[K-1] #인덱스 값이라 -1
    total_score.sort()
    idx = N - total_score.index(std_score) 
    #순서가 작은 점수 우선이므로
    #reverse 가 기억이 안남...

    rank = ''
    rank_num = (N/10)
    if 0 < idx <= rank_num:
        rank = 'A+'
    elif idx <= (rank_num*2):
        rank = 'A0'
    elif idx <= (rank_num*3):
        rank = 'A-'
    elif idx <= (rank_num*4):
        rank = 'B+'
    elif idx <= (rank_num*5):
        rank = 'B0'
    elif idx <= (rank_num*6):
        rank = 'B-'
    elif idx <= (rank_num*7):
        rank = 'C+'
    elif idx <= (rank_num*8):
        rank = 'C0'
    elif idx <= (rank_num*9):
        rank = 'C-'
    else:
        rank = 'D0'

    print(f"#{case_num} {rank}")
