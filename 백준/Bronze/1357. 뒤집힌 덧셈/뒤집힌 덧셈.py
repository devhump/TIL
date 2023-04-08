
a,b = input().split()

a = int(a[::-1])
b = int(b[::-1])

c = str(a+b)
c = str(int(c[::-1]))
print(c)