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