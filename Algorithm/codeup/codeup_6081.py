# a:97 f:102
# A:65 F: 70

# 내 풀이
# char = input()

# if char == 'A':
#   hex_num = 10
# elif char == 'B':
#   hex_num = 11
# elif char == 'C':
#   hex_num = 12
# elif char == 'D':
#   hex_num = 13
# elif char == 'E':
#   hex_num = 14
# elif char == 'F':
#   hex_num = 15

# for i in range(1, 16):
#   print('%X'%hex_num, '*%X'%i, '=%X'%(hex_num*i), sep='')



# 인터넷 풀이
a = int(input(), 16)

print(a, type(a))

# for i in range(1, 16):
#     print("%X*%X=%X" % (a, i, a*i))
