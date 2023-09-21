# BOJ_11720 / 숫자들의 합

N = int(input())
num_str = input()

result = 0
for i in range(N):
    result += int(num_str[i])

print(result)
