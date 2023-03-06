# BOJ_17249 태보태보 총난타

# face = input()

# cnt_left = 0
# for char in face:
#     if char == "@":
#         cnt_left += 1
#     elif char == "(":
#         break

# idx = face.index(")")

# cnt_right = 0
# for char in face[idx + 1 :]:
#     if char == "@":
#         cnt_right += 1

# print(cnt_left, cnt_right)

face = input()

idx_L = face.index("(")
idx_R = face.index(")")

print(face[:idx_L].count("@"), face[idx_R + 1 :].count("@"))
