num = list(map(int, input().split()))
num.sort()

n = (num[0]-1) % 4
m = (num[0]-1) // 4 

n2 = (num[1]-1) % 4
m2 = (num[1]-1) // 4

print(abs(n2-n) + abs(m2-m))