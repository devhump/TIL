# BOJ_1076 저항
import sys
sys.stdin = open("BOJ_1076_input.txt", "r")

import sys 
input = sys.stdin.readline

res_dict1 = {
    'black': '0', 
    'brown':'1', 
    'red':'2', 
    'orange':'3', 
    'yellow':'4', 
    'green': '5', 
    'blue':'6', 
    'violet':'7', 
    'grey':'8', 
    'white':'9'
    }

res_dict2 = {
    'black': 1, 
    'brown': 10, 
    'red': 100, 
    'orange':1000, 
    'yellow':10000, 
    'green': 100000, 
    'blue': 1000000, 
    'violet':10000000, 
    'grey':100000000, 
    'white':1000000000
    }

# print(res_dict2['white'])

res1 = input()
res2 = input()
res3 = input()

print(int(res_dict1[res1]+res_dict1[res2])*res_dict2[res3])

