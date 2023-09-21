a, b, c = map(int, input().split())

# a, b, c = 1, 2, 3

if a == b and b == c:
    print(10000+ (a*1000))
elif a == b:
    print(1000 + a*100)
elif b == c:
    print(1000 + c*100)
elif a == c:
    print(1000 + c*100)
else:
    nums = [a, b, c]
    # print(max(nums))

    print(max(nums)*100)

