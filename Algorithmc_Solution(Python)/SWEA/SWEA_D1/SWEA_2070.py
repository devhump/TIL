import sys
sys.stdin = open("SWEA_2070.txt", "r")

T = int(input())
cnt = 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):

    a = map(int, input().split())
    a = list(a)
    
    cnt += 1

    if a[0] == a[1]:
        print(f"#{cnt} =")
    elif a[0] > a[1]:
        print(f"#{cnt} >")
    elif a[0] < a[1]:
        print(f"#{cnt} <")

        
