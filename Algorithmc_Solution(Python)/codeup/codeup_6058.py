a, b = map(int, input().split())
# a, b = 0 , 0
# a, b = 0 , 1

if not bool(a):
  if not bool(b):
    print(True)
  else:
    print(False)
else:
  print(False)

# if a == 0 and b == 0:
#   print(True)
# else:
#   print(False)