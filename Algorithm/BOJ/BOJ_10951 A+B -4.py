# BOJ_10951 A+B -4
import sys
sys.stdin = open('BOJ_10951_input.txt', 'r')

while True:
	try:
		a, b = map(int, input().split())
		print(a+b)
	except EOFError:
		break