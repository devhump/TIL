# import sys
# sys.stdin = open("SWEA_1976_input.txt", "r")

T = int(input())
cnt = 0

for i in range(T):
    H = 0 #초기화 하는 변수/ 아닌변수 확인!
    cnt += 1
    H1, M1, H2, M2 = map(int, input().split())

    if (M1 + M2) >= 60:
        M = (M1 + M2) - 60
        H += 1
    else:
        M = (M1 + M2)

    H = H + (H1 + H2)

    if H > 12:
        H -= 12        

    print(f"#{cnt} {H} {M}")
