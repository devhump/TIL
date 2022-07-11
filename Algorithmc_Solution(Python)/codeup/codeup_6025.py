# 입력받은 숫자에 5를 더한 결과를 출력하세요
num = input()
print(num + 5) #오류 발생!
#input으로 받은 인자가 모두 string (data type) 로 저장됨.
# 따라서 숫자로 활용하기 위해 int로 명시적 형 변환 필요!


print(int(num) + 5) 