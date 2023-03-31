# BOJ_10798_세로읽기

import sys
sys.stdin = open("BOJ_10798_input.txt", "r")

Alist = list(input())
Blist = list(input())
Clist = list(input())
Dlist = list(input())
Elist = list(input())

result = ""

Max_len = max(len(Alist), len(Blist), len(Clist), len(Dlist), len(Elist))

# print(Alist)
for i in range(Max_len):
    if Alist:
        result += Alist.pop(0)
    if Blist:
        result += Blist.pop(0)
    if Clist:
        result += Clist.pop(0)
    if Dlist:
        result += Dlist.pop(0)
    if Elist:
        result += Elist.pop(0)

print(result)
            