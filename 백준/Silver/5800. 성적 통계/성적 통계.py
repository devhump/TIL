for t in range(int(input())):
    temp_li = list(map(int, input().split()))

    n = temp_li.pop(0)
    res = []
    res.append(max(temp_li))
    res.append(min(temp_li))
    temp_li.sort()
    
    max_gap = 0
    for i in range(n-1):
        if (temp_li[i+1] - temp_li[i]) > max_gap:
            max_gap = temp_li[i+1] - temp_li[i]

    print(f"Class {t+1}")
    print(f"Max {res[0]}, Min {res[1]}, Largest gap {max_gap}")