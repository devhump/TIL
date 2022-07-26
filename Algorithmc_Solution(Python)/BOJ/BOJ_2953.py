#나는 요리사다

import sys
sys.stdin = open("BOJ_2953_input.txt")

T = 5
score_list = []

for i in range(T):
    score_num = map(int, input().split())
    score_list.append(sum(score_num))

# print(score_list)
highest_score = max(score_list)
human_num = score_list.index(highest_score)

print(human_num+1, highest_score)

# for i in range(T):
