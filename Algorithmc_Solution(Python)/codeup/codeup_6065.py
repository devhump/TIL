a, b, c = map(int, input().split())

num_list = [a, b, c]

for num in num_list:
  if num % 2 == 0:
    print(num)