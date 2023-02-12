num_list = []
for i in range(9):
    num_list.append(int(input()))

max_ = max(num_list)
print(max_)
print(num_list.index(max_) + 1)