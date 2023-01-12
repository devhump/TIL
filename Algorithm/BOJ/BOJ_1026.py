# BOJ_1026 보물 / 그리디

num_cnt = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort(reverse=True)
B_list.sort()

total_sum = 0
for i in range(num_cnt):
    total_sum += A_list[i] * B_list[i]

print(total_sum)

# 문제상에서 수열 B를 재배치 하지 말라고 하는 게 함정이다
# 각각 A,B 리스트를 각각 내림차순, 오름차순으로 정렬한 후
# A의 큰수, B의 작은수 순서대로 곱한 값의 합을 구한다.
