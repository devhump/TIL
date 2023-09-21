T = int(input())

# T = 2

for t in range(1, T+1):
  star = '* '

  star *= T

  if t % 2 != 0:
    print(star)
  else:
    print(' '+star)