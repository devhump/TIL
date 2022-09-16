h, b, c, s = map(int, input().split())
# h, b, c, s = 44100, 16, 2, 10


result = ((((h*b*c*s)/8)/1024)/1024)
# print(result) #1.682281494140625

print(round(result, 1),'MB')
#소숫점 2째 자리에서 반올림
