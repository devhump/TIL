# BOJ_7785 회사에 있는 사람
import sys
sys.stdin = open("BOJ_7785_input.txt", "r")
num = int(input())

inwork = {}
for i in range(num):
    temp = []
    temp = list(map(str, input().split()))
    inwork[temp[0]] = temp[1]

result = []
for item in inwork.items():
    if item[1] == "enter":
        result.append(item[0])

result.sort(reverse=True)
for i in range(len(result)):
    print(result[i])

# ? 훨씬 간결하고 빠르다!
# import sys
# input = sys.stdin.readline
# a = {}
# for i in range(int(input())):
#   name, b = input().rstrip().split()
#   if b == 'leave':
#     del a[name]
#   else:
#     a[name] = b
# a1 = sorted(a.items(),reverse= True)
# for key,value in a1:
#   print(key)