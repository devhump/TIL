# SWEA_2005 파스칼의 삼각형
# * 처음에 너무 어렵게 생각했나보다.
# * 입력받는 최대값이 10이라 그냥 미리 다 구해놓고,
# * 필요한 만큼만 출력하는 식으로 구현했다. 

T = int(input())

for t in range(T):
    N = int(input())

    pascal = [[1], [1, 1]] # 1, 2번줄은 미리 입력해두고

    for i in range(2, 10):
        temp = [1] # 모든 줄의 시작은 항상 1
        for j in range(len(pascal[i-1])-1): # @ 이전 줄의 개수-1 
            temp.append(pascal[i-1][j]+pascal[i-1][j+1]) 
            # @ 이전 줄의 처음부터 두개씩 더하면된다.
        temp.append(1) # 모든 줄의 마지막은 항상 1
        pascal.append(temp) # * 각 줄을 완성 후 pascal에 저장

    print(f'#{t+1}')
    for k in range(N):
        for num in pascal[k]:
            print(num, end=' ')
        print()