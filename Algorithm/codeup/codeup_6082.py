num_369 = int(input())

for i in range(1, num_369+1):
  
  if '3' in str(i) or '6' in str(i) or '9' in str(i):
    print('X', end=' ')
  else:
    print(i, end=' ') 