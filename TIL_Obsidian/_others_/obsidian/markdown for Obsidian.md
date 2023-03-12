#Obsidian 

- 기본 마크다운 내용 정리 👉 [KDT_markdown+](obsidian://open?vault=TIL_Obsidian&file=KDT%2Fmarkdown%2Fmarkdown%20(%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4)%20%2B)
- 수학-공식 관련 표기법 👉 [[LaTeX]]

##### 개별문서
- [[Callout]]
- [[Diagram]]
- [Obsidian Guide - Link notes](obsidian://open?vault=Obsidian%20Sandbox&file=Guides%2FLink%20notes)

>[!note] 목차
[1. Blockquote](#1.%20Blockquote)
[2. Code block](#2.%20Code%20block)
[3. Comment](#3.%20Comment)
[4. Embeds](#4.%20Embeds)
[5. Emphasis](#5.%20Emphasis)
[6. footnote](#6.%20footnote)
[7. Resizing image](#7.%20Resizing%20image)
[8. Link](#8.%20Link)
[9. Math](#9.%20Math)
[10. Table](#10.%20Table)
[11. Task](#11.%20Task)


### 1. Blockquote

```

> 인용 문구
> 인용인용
> 인용한다.

\- ramy jo, 2023
```

> 인용 문구
> 인용인용
> 인용한다.

\- ramy jo, 2023

---

### 2. Code block

```md
    Text indented with a tab is formatted like this, and will also look like a code block in preview. 
```


	Text indented with a tab is formatted like this, and will also look like a code block in preview. 

---

### 3. Comment
- 드래그 해서 `ctrl` + `/`
- 같은 줄 내에서 %%주석처리%% 하기
- 여러줄 일 때
%%
주석처리 하기
%%

![](asset/Pasted%20image%2020230222121902.png)

---

### 4. Embeds
- `![[삽입하고 싶은 문서 제목 or 파일명]]`
```md
![[Plugins makes Obsidian special for you]]
```

#### 다른 문서의 특정 문단을 Embed 하고 싶은 경우
1) `[[ ]]` 를 입력하고, 해당 문서의 제목을 입력한다.
![](assets/Pasted%20image%2020230226003835.png)

2) 해당문서를 찾아, 포인터가 올려져 있는 상태에서
	1) 제목을 찾을 경우 `#`를, 
	2) 문단을 찾을 경우 `^`를 입력한다.

![](assets/Pasted%20image%2020230226003908.png)

3) 이후 해당 내용을 찾아 `enter`를 누르면 해당 내용이 삽입되는 걸 확인 할 수 있다. 

---
### 5. Emphasis
- 이탤릭체 + 부분 강조 섞어 쓰기
```md
_You **can** combine them_
```

▶️  _You **can** combine them_

---
### 6. footnote
- inline 주석 처리도 가능하다. 

```markdown
You can also use inline footnotes. ^[notice that the carat goes outside of the brackets on this one.]
```

- You can also use inline footnotes. ^[notice that the carat goes outside of the brackets on this one.]
- ![](asset/Pasted%20image%2020230222125820.png)

---

### 7. Resizing image
Example of this above image resized to 200 pixels wide:

```md
![Obsidian|200](https://obsidian.md/images/banner.png)
```

![Obsidian|200](https://obsidian.md/images/banner.png)


---

### 8. Link
#### external links
```
http://obsidian.md - automatic!
```

- http://obsidian.md - automatic!

#### Obsidian URI links

Obsidian URI links can be used to open notes in Obsidian either from another Obsidian vault or another program.

```
[📑 devhump's TIL Index](obsidian://open?vault=TIL_Obsidian&file=%F0%9F%93%91%20devhump's%20TIL%20Index)
```
[📑 devhump's TIL Index](obsidian://open?vault=TIL_Obsidian&file=%F0%9F%93%91%20devhump's%20TIL%20Index)

- 절대 결로를 사용한 주소도 사용 가능

#### Escaping
- 문서 제목에 띄어쓰기가 있다면, 공백 자리에 `%20`를 쓰거나, `<>`로 제목을 감싸서 사용 하는 것도 가능하다. 
```
[Callout 1](Callout.md)
[markdown for obsidian 1](markdown%20for%20obsidian.md)

[Callout 2](<Callout>)
[markdown for obsidian 2](<markdown for obsidian>)
```

[Callout 1](Callout.md)
[markdown for obsidian 1](markdown%20for%20Obsidian.md)

[Callout 2](Callout.md)
[markdown for obsidian 2](markdown%20for%20Obsidian.md for obsidian>)

---
### 9. Math
- 수학-공식 관련 표기법 👉 [[LaTeX]]

```md
$$\begin{vmatrix}a & b\\
c & d
\end{vmatrix}=ad-bc$$
```

$$\begin{vmatrix}a & b\\
c & d
\end{vmatrix}=ad-bc$$

- You can also do inline math like `$e^{2i\pi} = 1$ `.

- You can also do inline math like $e^{2i\pi} = 1$ .

- Obsidian uses [Mathjax](http://docs.mathjax.org/en/latest/basic/mathjax.html). You can check which packages are supported in Mathjax [here](http://docs.mathjax.org/en/latest/input/tex/extensions/index.html).

---
### 10. Table
```md
First Header | Second Header
------------ | ------------
Content from cell 1 | Content from cell 2
Content in the first column `:`| Content in the second column
```

First Header | Second Header
------------ | ------------
Content from cell 1 | Content from cell 2
Content in the first column `:`| Content in the second column

- 이렇게만 표현해도 표를 작성할 수 있다. 
- 표의 정렬에 콜론(colon, `:`)을 이용하기 때문에, 표 내에서 `:`를 쓰려면 좌우로 백틱(backtick)을 붙여준다. 

```md
First Header | Second Header
------------ | ------------
[Callout](Callout.md)	|  [[Callouts\|Callouts]]
```

First Header | Second Header
------------ | ------------
[Callout](Callout.md)	|  [[Callouts\|Callouts]]

- 표내에 링크를 쓰기 위해선 `[Callout](Callout.md)` 또는	`[[Callouts\|Callouts]]` 표기법을 이용하면 된다.

---
### 11. Task
```md
- [x] #tags, [links](), **formatting** supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [?] this is also a complete item (works with every character)
- [ ] this is an incomplete item
- [ ] tasks can be clicked in Preview to be checked off
```

- [x] #tags, [links](), **formatting** supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [?] this is also a complete item (works with every character)
- [ ] this is an incomplete item
- [ ] tasks can be clicked in Preview to be checked off