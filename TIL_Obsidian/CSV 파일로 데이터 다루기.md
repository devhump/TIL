
### CSV 파일로 데이터 다루기

#### CSV형 리스트
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


#### 만든 함수 모듈화 하기
- Anaconda3 / Lib 폴더 내에 저장
```python
# usecsv.py
import csv, os
# 새롭게 시작할 때, csv 모듈을 먼저 임포트 합니다.
def opencsv(filename):
	f = open(filename, 'r')
	reader = csv.reader(f)
	output = []
	for i in reader:
		output.append(i)
	return output
# opencsv() 함수에서는 f를 파일 객체를 직접 open하는 방식을 사용했습니다. 

def writecsv(filename, the_list):
	with open(filename, 'w', newline = '') as f:
		a = csv.writer(f, delimiter = ',')
		a.writerows(the_list)
# writerows() 함수에서는 with문을 사용해 코드 길이가 조금 더 짧습니다. 

```

#### 숫자 형식 변경(str → float)
```markdown
# popSeoul

Gu,Korean,Foreigner,Senior
Total,"9,740,398","285,529","1,468,146"
Jongrogu,"151,767","11,093","27,394"
Jongru,"126,409","10,254","23,025"
Yongsangu,"228,830","16,159","38,531"
Seongdonggu,"303,158","8,132","43,662"
Kwangjingu,"352,692","15,645","47,347"
Dongdaemoongu,"346,551","17,228","58,764"
Jungranggu,"398,812","4,964","64,449"
Seongbukgu,"441,590","12,524","70,204"
Gangbukgu,"314,090","3,785","59,808"
Dobonggu,"335,280","2,314","58,070"
Nowonggu,"535,282","4,547","79,968"
Eunpyonggu,"481,663","4,496","79,957"
Seodaemungu,"310,069","14,020","51,708"
Mapogu,"373,629","11,976","51,961"
Yangcheongu,"459,849","4,082","60,487"
Gangseogu,"593,708","6,532","82,937"
Gurogu,"406,748","33,102","64,952"
Guemcheongu,"233,371","19,497","37,191"
Youngdeungpogu,"368,402","34,076","57,350"
Dongjakgu,"397,618","12,869","61,607"
Kwanakgu,"502,117","17,836","74,518"
Seoucheogu,"431,027","4,231","56,455"
Gangnamgu,"544,028","5,015","70,029"
Songpagu,"677,489","6,849","86,062"
Gangdonggu,"426,219","4,303","61,710"
```


```python
>>> import os, re
>>> import usecsv
>>> os.chdir(r'C:\Users\user\python')
>>> total = usecsv.opencsv('popSeoul.csv')

>>> for i in total[:5]:
>>> 	print(i)


### 숫자 중 쉼표 제거해서 float 형으로 변경
>>> import re
>>> i = total[2]
>>> i

>>> k = []
>>> for j in i:
>>> 	if re.search('\d', j):
>>> 		k.append(float(re.sub(',','', j)))
>>> 	else:
>>> 		k.append(j)
>>> k

### 문자가 섞인 원소 골라내기
>>> k = []
>>> for j in i:
>>> 	if re.search('[a-z가-힣]', j): 
>>> 	# 알파벳 또는 한글이 있다면 그대로 저장
>>> 		k.append(j)
>>> 	else:
>>> 		k.append(float(re.sub(',','', j)))
```

```python
import re

def swithch(listName):
	for i in listName:
		for j in i:
			try:
				i[i.index(j)] = float(re.sub(',', '', j))
			except:
				pass
	return listName
```
