# BOJ_10101 삼각형 외우기

# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

triangle = []
for _ in range(3):
    triangle.append(int(input()))

triangle.sort()

if sum(triangle) == 180:
    if triangle[0] == 60 and triangle[1] == triangle[2]:
        print("Equilateral")
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2]:
        print("Isosceles")
    elif triangle[0] != triangle[1] and triangle[1] != triangle[2]:
        print("Scalene")
else:
    print("Error")