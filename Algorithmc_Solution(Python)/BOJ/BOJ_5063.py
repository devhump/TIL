#BOJ_5063. TGN

import sys
sys.stdin = open("BOJ_5063_input.txt")

T = int(input())

# r == 광고를 하지 않았을 때의 수익
# e == 광고를 했을 때의 수익
# c == 광고비용

Do_ad = "advertise" #광고를 해야한다
same_ad = "does not matter" #수익에 차이가 없다
No_ad = "do not advertise" #하지 않아야 한다

for i in range(T):
    r, e , c = map(int, input().split())
    sum_ad = (e - r - c)

    if sum_ad == 0:
        print(same_ad)
    elif sum_ad > 0:
        print(Do_ad)
    elif sum_ad < 0:
        print(No_ad)