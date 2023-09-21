# BOJ_2789 유학금지

cam_univ = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]

word = input()

for char in word:
    if char in cam_univ:
        word = word.replace(char, "")

print(word)
