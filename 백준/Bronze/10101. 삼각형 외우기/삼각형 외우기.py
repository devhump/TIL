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