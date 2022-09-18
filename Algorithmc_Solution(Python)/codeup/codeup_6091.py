a, b, c = map(int, input().split())
# a, b, c = 3, 7, 9

# d = 1
# while d%a!=0 or d%b!=0 or d%c!=0 :
#   d += 1
# print(d)

d = 1
while True:

    if d % a == 0 and d % b == 0 and d % c == 0:
        break
    d+=1
print(d)