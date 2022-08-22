# HPHK 문제 01. 수 구분하기+

# num = int(input())
num = 267
#test case
# 267 : 참
# 264 : 참
# 14 : 거짓

if num % 2 == 0:
    if num % 3 == 0:
        print("참")
    else:
        print("거짓")
else:
        print("거짓")