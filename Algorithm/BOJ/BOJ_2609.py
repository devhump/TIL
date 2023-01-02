# 최대 공약수, 최소공배수 계산기
# https://hi098123.tistory.com/155

a, b = map(int,input().split())

a_divisor = []
b_divisor = []

# max_div 최대공약수
# min_mul 최소공배수 
# 각 숫자별 약수 리스트 생성
################################
for i in range(1, a+1): #본인도 포함되야 해서!
    if (a) % i == 0:
        a_divisor.append(i)

for i in range(1, b+1):
    if (b) % i == 0:
        b_divisor.append(i)

for num in a_divisor:
    for num2 in b_divisor: # 두개의 리스트가 생성 단계에서부터 정렬되어있음
        if num == num2:
            max_div = num # 값 덮어쓰기를 하다보면 가장 큰 값 저장

min_mul = int((a * b)/max_div) # (두 수의 곱 / 최소공약수) == 최소공배수

print(max_div)
print(min_mul)




