import sys
sys.stdin = open("SWEA_2029.txt", "r")

T = int(input())
cnt = 0 

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    
    cnt += 1

    a = map(int, input().split())
    a = list(a)
    
    temp1 = a[0] // a[1] #몫
    temp2 = a[0] % a[1] #나머지

    print(f"#{cnt} {temp1} {temp2}")