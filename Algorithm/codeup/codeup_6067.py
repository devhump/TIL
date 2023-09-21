a = int(input())


if a < 0: # a가 음수이면
  if a % 2 == 0:
    print("A") # 음수 & 짝수
  else:
    print("B") # 음수 & 홀수
else: # a가 양수이면
  if a % 2 == 0 :
    print("C") # 양수 & 짝수
  else:
    print("D") # 양수 & 홀수