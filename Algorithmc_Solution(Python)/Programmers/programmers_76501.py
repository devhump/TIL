# <음양 더하기>

# input & output

absolutes = [4, 7, 12]
signs = [True, False, True]

# absolutes = [1,2,3]
# signs = [False, False, True]

def solution(absolutes, signs):
	answer = 0
	
	for i in range(len(absolutes)):
		if signs[i] == True: # True면 양의 정수라 pass				pass
			answer += absolutes[i]
		else:            	 # False면 -1 곱해서 양수로 변환
			answer += (absolutes[i]*(-1))
	
	return answer

if __name__ == '__main__':
    
	print(solution(absolutes, signs))


# #######################################################
# # 정성껏 쓴 오답
# #######################################################

# import sys
# sys.stdin = open("programmers_76501_input.txt")

# def solution(absolutes, signs):
# 	answer = 0
	
# 	for i in range(len(signs)):
# 		if signs[i] == "true" : # 'true'면 1로 교체
# 			signs[i] = 1
# 		else:				   # 'false'면 -1로 교체
# 			signs[i] = -1
			
# 	for i in range(len(absolutes)):
# 		answer += (absolutes[i] * signs[i])

# 	return answer



# if __name__ == '__main__':

# 	absolutes = list(map(int, input().split()))
# 	signs = list(map(str, input().split()))
    
# 	print(solution(absolutes, signs))

