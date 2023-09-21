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