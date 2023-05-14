# SWEA_1928. Base64 Decoder

base_64_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

T = int(input())

for t in range(T):
    temp_str = input()

    long_str = ""
    while temp_str:
        a = base_64_str.index(temp_str[0])
        long_str += bin(a)[2:].zfill(6)
        temp_str = temp_str.replace(temp_str[0],"", 1)

    ans = ""
    while long_str:
        ans += chr(int(long_str[:8], 2))
        long_str = long_str.replace(long_str[:8],"", 1)
        
    print(f'#{t+1} {ans}')

