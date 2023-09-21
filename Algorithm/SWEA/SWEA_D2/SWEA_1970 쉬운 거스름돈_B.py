# SWEA_1970 쉬운 거스름돈
# 50,000 원 0
# 10,000 원 1
# 5,000 원 2 
# 1,000 원 3
# 500 원 4 
# 100 원 5 
# 50 원 6 
# 10 원 7

# @ 통과
T = int(input())

for t in range(T):

    won = int(input())

    won_list = [0] * 8

    if won >= 50000:
        N = (won // 50000)
        won -= 50000*N
        won_list[0] = N
    if won >= 10000:
        N = (won // 10000)
        won -= 10000*N
        won_list[1] = N    
    if won >= 5000:
        N = (won // 5000)
        won -= 5000*N
        won_list[2] = N    
    if won >= 1000:
        N = (won // 1000)
        won -= 1000*N
        won_list[3] = N
    if won >= 500: 
        N = (won // 500)
        won -= 500*N
        won_list[4] = N
    if won >= 100: 
        N = (won // 100)
        won -= 100*N
        won_list[5] = N
    if won >= 50: 
        N = (won // 50)
        won -= 50*N
        won_list[6] = N
    if won >= 10: 
        N = (won // 10)
        won -= 10*N
        won_list[7] = N

    print(f'#{t+1}')
    for i in range(8):
        print(won_list[i], end=" ")
    print()