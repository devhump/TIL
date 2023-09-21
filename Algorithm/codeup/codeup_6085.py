w, h, b = map(int, input().split())
# w, h, b = 1024, 768, 24 #2.25 MB
# w, h, b = 800, 600, 24 # 1.37 MB
# w, h, b = 100, 100, 4 # 0.00 MB


result = ((((w*h*b)/8)/1024)/1024)
# print(result) #2.25

print(f"{round(result, 2):.2f} MB")
#소숫점 3째 자리에서 반올림

## 소수점 출력 방법
# print(f"{result:.2f} MB")
# print("%0.2f MB" % result)
# print('%.2f'%result,"MB")