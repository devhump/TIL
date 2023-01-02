T = int(input())

# T = 5

cnt = 1
for t in range(T):
  result = ''
  
  sp = ' ' 
  star = '*'

  result = (sp*(T-cnt)) + (star*cnt)

  print(result)
  cnt += 1