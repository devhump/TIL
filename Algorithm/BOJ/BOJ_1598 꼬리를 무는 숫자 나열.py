# BOJ_1598 꼬리를 무는 숫자 나열

num = list(map(int, input().split()))
num.sort()
# 좌표 개념으로 접근하기 위해 두 수에 -1씩 빼준다. (원점 0,0)
n = (num[0]-1) % 4
m = (num[0]-1) // 4 
print(n,m)
n2 = (num[1]-1) % 4
m2 = (num[1]-1) // 4
print(n2,m2)
print(abs(n2-n) + abs(m2-m))