num = int(input())

result = 0
for i in range(0, num+1):
  
  if i % 2 == 0:
    result += i
  
print(result)