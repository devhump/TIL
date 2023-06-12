
### CSV 파일로 데이터 다루기

```md
csv형 리스트 = [[1행], [2행], ..., [n행]]
```

#### CSV 파일 읽어들이는 방법
```python
>>> import csv, os
>>> os.chdir(r'C:\Users\user\python')
# os.getcwd()
>>> f.open('a.csv', 'r')
# f.open('a.csv', 'r', encoding = 'utf=8')

>>> new = csv.reader(f)
>>> new
<_csv.reader object at 0x000001F3AEDE88E0>
>>> for i in new:
>>> 	print(i)

>>> a_list = []
>>> for i in new:
		print(i)
		a_list.append(i)
>>> a_lsit
[]

>>> f.seek(0) # 커서 맨 앞으로 옮겨줘야 
0
>>> for i in new:
		print(i)
		a_list.append(i)
```

##### CSV 파일 읽어들이는 방법(함수화)
```python
def opencsv(filename):
	f = open(filename, 'r')
	reader = csv.reader(f)
	output = []
	for i in reader:
		output.append(i)
	return output
```


#### CSV 파일 쓰는 방법
```python
>>> a = [['구','전체','내국인','외국인'],
	['관악구','519864','502089','17775'],
	['강남구','547602','542498','5104'],
	['송파구','686181','679247','6924'],
	['강동구','428547','424235','4312']]

>>> f = open('abc.csv', 'w', newline= '')
>>> csvobject = csv.writer(f, delimiter = ',')
>>> csvobject.writerows(a)
>>> f.close()
```

##### CSV 파일 쓰는 방법(함수화)
```python
def writecsv(filename, the_list):
# 첫번째 변수는 만들 파일 이름, 두번째는 CSV형 리스트를 저장한 객
	with open(filename, 'w', newline= '') as f:
		a = csv.writer(f, delimiter = ',')
		a.writerows(the_list)
```

