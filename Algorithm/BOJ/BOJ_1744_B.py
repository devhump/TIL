# BOJ_1744 수묶기 / 그리디

N = int(input())

numbers = []
for i in range(N):
    numbers.append(int(input()))

numbers.sort()

result = 0
while N > 1:
    temp1 = numbers.pop()
    temp2 = numbers.pop()

    if temp1 == 1 or temp2 == 1:
        result += temp1 + temp2
    elif temp1 < 0 and temp2 < 0:
        result += temp1 * temp2
    elif temp1 == 0:
        if temp2 >= 0:
            result += temp1 + temp2
        else:
            result += temp1 * temp2
    elif temp2 == 0:
        if temp1 >= 0:
            result += temp1 + temp2
        else:
            result += temp1 * temp2
    else:
        result += temp1 * temp2

    N -= 2

if N == 1:
    result += numbers[0]

print(result)
