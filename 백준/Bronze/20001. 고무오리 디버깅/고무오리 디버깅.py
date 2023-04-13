start = input()

result = 0

while True:
    
    temp = input()
    if "고무오리 디버깅 끝" == temp:
        break

    if temp == "문제":
        result += 1
    elif temp == "고무오리":
        if result > 0:
            result -= 1
        else:
            result += 2

if result >= 1:
    print("힝구")
else:
    print("고무오리야 사랑해")