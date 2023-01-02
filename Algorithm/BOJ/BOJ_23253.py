
import sys
sys.stdin = open("BOJ_23253_input.txt")

M, N = map(int, input().split())

book_dummy = []
book_list = []

for i in range(N):
    temp_dummy = int(input())
    temp_list = list(map(int, input().split()))

    book_dummy.append(temp_dummy)
    book_list.append(temp_list)

# print(book_dummy)
print(book_list)
print(book_list[1])
j = 0
final_list = []
for i in range(1, M+1):
    for j in range(N):
        temp_list = book_list[j]
        while(len(temp_list) > 1):
            # print(id(book_list[j].pop()))
            # print(id(temp_list))
            temp = temp_list.pop()

            if temp == i:
                final_list.append(temp)
            else:
                temp_list.append(temp)

print(final_list)


# 미완
