---
tags: [python, "-"]
---

![eunmerate 순회](../KDT/Python/파이썬%2002.%20제어문%20(Control%20Statement).md#eunmerate%20순회)

##### Enumerate 예시

```python
data=list(input().split('-'))
result=0

for i,d in enumerate(data):
	data[i]=(sum(list(map(int,d.split('+')))))

result=data[0]
for d in data[1:]:
	result-=d
  
print(result)
```

```python
# BOJ_11501 주식

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    answer = 0 #손익 계산 
    stock = 0 #주식 개수 
    for i, price in enumerate(data):
        if i == 0:
            if price<max(data):
                answer -= price
                stock += 1 
        else:
            right = max(data[i:])
            if price<right: #매수 
	            answer -= price
                stock += 1 
            elif price == right: #매도 
                answer += price*stock 
                stock = 0 
    print(answer)
```