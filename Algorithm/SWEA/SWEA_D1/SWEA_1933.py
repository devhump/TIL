# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

# input = 10
# output = 1 2 5 10

num = 10

num_divisor = []

for i in range(1,num+1):
    if (num % i) == 0:
        num_divisor.append(i)


for i in num_divisor:
    print(i, end=' ')