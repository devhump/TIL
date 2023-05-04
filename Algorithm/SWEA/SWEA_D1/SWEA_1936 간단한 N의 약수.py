# SWEA_1936 간단한 N의 약수

# num = int(input())
num = 10

for i in range(1, num+1):
    if 10 % i == 0:
        print(i, end=" ")