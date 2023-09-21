a, b, c = map(int, input().split())

# a, b, c = 0, 2, 4

num_list = [a, b, c]

for num in num_list:
  if num % 2 == 0:
    print("even")
  else:
    print("odd")