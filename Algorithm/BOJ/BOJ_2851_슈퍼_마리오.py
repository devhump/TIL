# BOJ_2851_슈퍼_마리오

import sys
sys.stdin = open("BOJ_2851_input.txt", "r")

result = 0 
mushrooms = []
for i in range(10):
    temp = int(input())

    result += temp
    mushrooms.append(result)

    if result >= 100:
        break

# print(mushrooms)
if mushrooms[-1] <= 100:
    print(mushrooms[-1])
elif abs(100 - mushrooms[-1]) == abs(100 - mushrooms[-2]):
    print(mushrooms[-1])
elif abs(100 - mushrooms[-1]) < abs(100 - mushrooms[-2]):
    print(mushrooms[-1])
else:
    print(mushrooms[-2])


## 처음에는 절대값(abs)를 생각하지 않아서 틀렸고, 
## 두번째는 10개의 숫자를 다 더했을 때 100보다 작은 경우를 
## 고려하지 않았음.