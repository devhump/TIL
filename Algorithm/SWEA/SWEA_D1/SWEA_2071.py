import sys
sys.stdin = open("SWEA_2071.txt", "r")

T = int(input())
cnt = 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):

    cnt += 1

    a = map(int, input().split())
    a = list(a)

    list_sum = 0
    average_result = 0

    for j in range(len(a)):
        list_sum += a[j]
        result = round(int(list_sum/len(a)))

    print(f"#{cnt} {result}")


############################################################
# 반올림 처리 필요!
############################################################

