T = 10
num = int(input())

rest = []

for i in range(T):
    num = int(input())
    rest.append(num % 42)

print(len(set(rest)))
