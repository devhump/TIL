# BOJ_11945 뜨거운 붕어빵


import sys
sys.stdin = open("BOJ_11945_input.txt", "r")

# ! 틀린 코드 
# n, m = map(int, input().split())

# matrix = [input().split() for _ in range(n)]

# for i in range(n):
#     print(matrix[i][0][::-1])

n, m = map(int, input().split())

matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(len(matrix[i])):
        print(matrix[i][j][::-1])
        # todo 혹시 붕어빵이 없는 경우를 고려해서 
        # 위와 같이 바꿨더니 통과~