# BOJ_2941. 크로아티아 알파벳 (internet)

croatia = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
word = input()

for char in croatia:
    word = word.replace(char, "*")
print(len(word))
