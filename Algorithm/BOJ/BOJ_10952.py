# 이 코드는 조건은 맞으나, 
# 0,0 일 때 0이 출력이됨
#
# a, b = 1, 1 #초기 설정만
# while ( a != 0 or b != 0 ):
#     a, b = map(int, input().split()) 

#     print(a+b)


while True:

    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    print(a+b)