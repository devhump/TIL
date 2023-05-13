# SWEA_1928. Base64 Decoder
# @ import가 안 된당...ㅠㅠ


import sys
sys.stdin = open('SWEA_1928_input.txt', 'r')

import base64
T = int(input())


for t in range(T):
    sitename_base64_str  = input()
    sitename_bytes = base64.b64decode(sitename_base64_str )
    sitename = sitename_bytes.decode('ascii')

    print(f'#{t+1} {sitename}')