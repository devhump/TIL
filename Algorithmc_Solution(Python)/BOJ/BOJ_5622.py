Dial_char = {
    "A":2,
    "B":2,
    "C":2,

    "D":3,
    "E":3,
    "F":3,

    "G":4,
    "H":4,
    "I":4,

    "J":5,
    "K":5,
    "L":5,

    "M":6,
    "N":6,
    "O":6,

    "P":7,
    "Q":7,
    "R":7,
    "S":7,

    "T":8,
    "U":8,
    "V":8,

    "W":9,
    "X":9,
    "Y":9,
    "Z":9
}

num_str = input()
time = 0

for i in range(len(num_str)):
    time += Dial_char[num_str[i]] + 1

# 숫자 1일 때 2초
# 숫자 2일 때 3초, 3일때 4초...
# 숫자 N일 때 N+1초

print(time)
