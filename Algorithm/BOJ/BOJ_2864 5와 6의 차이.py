# BOJ_2864 5와 6의 차이

num = list(map(int, input().split()))
# num = [1430, 4862]

num1 = str(num[0])
num2 = str(num[1])

# * replace는 항상 반환값을 받아서 활용!
num1 = num1.replace("6", "5")
num2 = num2.replace("6", "5")
print((int(num1)+int(num2)), end=" ")

num1 = str(num[0])
num2 = str(num[1])

num1 = num1.replace("5", "6")
num2 = num2.replace("5", "6")
print((int(num1)+int(num2)))
