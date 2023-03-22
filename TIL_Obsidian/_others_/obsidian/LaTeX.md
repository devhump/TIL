#### LaTeX ?
- 문서 작성 도구의 일종. 논문이나 출판물 등의 특수 형식 문서를 작성하는데 쓰이는 시스템. 자연과학이나 인문과학 중 수식, 그래프, 다이어그램을 많이 그리는 학자들에게 유용한 문서 저작도구이다.[^출처]
- LaTeX는 TeX의 확장성을 이용하여, TeX를 좀 더 쉽게 쓸 수 있도록 해준 매크로 집합으로도 볼 수 있다. 

[^출처]: 나무위키 - LaTex (https://namu.wiki/w/LaTeX#s-3)

### 목차
```ad-note
- [[#LaTeX ?|LaTeX ?]]
- [[#1. 표기법|1. 표기법]]
	- [[#1. 표기법#1) inline표기법|1) inline표기법]]
	- [[#1. 표기법#2) 문단 표기법|2) 문단 표기법]]
- [[#2. 사칙연산|2. 사칙연산]]
- [[#3. 분수 (fraction)|3. 분수 (fraction)]]
- [[#4. 수학공식, 수식번호|4. 수학공식, 수식번호]]
- [[#5. 괄호|5. 괄호]]
	- [[#5. 괄호#괄호 리사이즈|괄호 리사이즈]]
- [[#6. 위첨자(superscript), 아래첨자(subscript)|6. 위첨자(superscript), 아래첨자(subscript)]]
- [[#7. dots (줄임, 생략)|7. dots (줄임, 생략)]]
- [[#8. Root(루트, square root)|8. Root(루트, square root)]]
- [[#9. Factorial (팩토리얼)|9. Factorial (팩토리얼)]]
- [[#10. 집합(set)|10. 집합(set)]]
- [[#11. 삼각함수, sin, cos, tan|11. 삼각함수, sin, cos, tan]]
- [[#12. 원주율 파이(pi)|12. 원주율 파이(pi)]]
- [[#13. 각도|13. 각도]]
- [[#14. 로그(log)|14. 로그(log)]]
- [[#15. 행렬 (matrix)|15. 행렬 (matrix)]]
- [[#16. 벡터, 스칼라 (Vector, Scalar)|16. 벡터, 스칼라 (Vector, Scalar)]]
- [[#17. 논문에 자주 나오는 기호|17. 논문에 자주 나오는 기호]]
	- [[#17. 논문에 자주 나오는 기호#17-1. 특수문자|17-1. 특수문자]]
	- [[#17. 논문에 자주 나오는 기호#17-2. 관계연산자|17-2. 관계연산자]]
	- [[#17. 논문에 자주 나오는 기호#17-3. 논리기호|17-3. 논리기호]]
	- [[#17. 논문에 자주 나오는 기호#17-4. 집합기호|17-4. 집합기호]]
	- [[#17. 논문에 자주 나오는 기호#17-5. 기타|17-5. 기타]]
- [[#18. 적분 (integral)|18. 적분 (integral)]]
- [[#19. 미분 (differential)|19. 미분 (differential)]]
- [[#20. 극한(limit)|20. 극한(limit)]]
- [[#21. 시그마(for)|21. 시그마(for)]]
```

#### 1. 표기법

##### 1) inline표기법
```
$a_i$
```
- $a_i$

##### 2) 문단 표기법
```
$$a_i$$
```
$$a_i$$

#### 2. 사칙연산
```
$$1 + 1 = 2$$
$$2 - 1 = 1$$
$$2 \times 2 = 4$$
$$2 \div 2 = 1$$
```

- $1 + 1 = 2$
- $2 - 1 = 1$
- $2 \times 2 = 4$
- $2 \div 2 = 1$

#### 3. 분수 (fraction)
```
$\frac{1}{2}$
$^1/_2$
```
- $\frac{1}{2}$
- $^1/_2$

#### 4. 수학공식, 수식번호
```
$X_{1,j} \mathbf{F}X_{2,j} = 0, \tag{1}$
```
- $X_{1,j} \mathbf{F}X_{2,j} = 0, \tag{1}$

#### 5. 괄호
```
$(1+2)$
$\{1+2\}$
$[1+2]$

자동괄호 리사이즈
$\left(\frac{2}{3}\right)$

수동괄호 리사이즈
$\Bigg( \bigg( \Big( \big( ( ) \big) \Big) \bigg) \Bigg)$
```

- $(1+2)$
- $\{1+2\}$
- $[1+2]$

##### 괄호 리사이즈
- 자동 괄호 리사이즈
	+ 자동으로 괄호의 리사이즈가 되기 위해서는 “left”, “right” 문자를 좌우로 넣어줍니다.
- 수동괄호 리사이즈
	-  big, Big, bigg, Bigg 문자를 사용하면 수동으로 괄호 사이즈를 조절할 수 있습니다.
```
$\left(\frac{2}{3}\right)$

$\Bigg( \bigg( \Big( \big( ( ) \big) \Big) \bigg) \Bigg)$
```
- $\left(\frac{2}{3}\right)$
- $\Bigg( \bigg( \Big( \big( ( ) \big) \Big) \bigg) \Bigg)$

#### 6. 위첨자(superscript), 아래첨자(subscript)
```
$8^8=64$
$a_1, a_2, a_3$
```
- $8^8=64$
- $a_1, a_2, a_3$

#### 7. dots (줄임, 생략)
```
$\dots$
$\cdots$
$\vdots$
$\ddots$
```
 - $\dots$  %%가운데를 기준으로 점을 표기%%
 - $\cdots$ 
- $\vdots$ %%세로로 점을 표기(행렬, 매트릭스 내부)%%
- $\ddots$  %%대각선을 점으로 표기(행렬, 매트릭스 내부)%%

#### 8. Root(루트, square root)
```
$\sqrt{2}$
```
- $\sqrt{2}$

#### 9. Factorial (팩토리얼)
```
$n!$
$n! = 1 \times 2 \times 3 \times \ldots n$
```
- $n!$
- $n! = 1 \times 2 \times 3 \times \ldots n$

#### 10. 집합(set)
```
# 합집합 
$$\{a,b,c\} \cup \{d,e\} = \{a,b,c,d,e\}$$

# 교집합
$$\{a,b,c\} \cap \{a,b,d\} = \{a,b\}$$

```
- $\{a,b,c\} \cap \{a,b,d\} = \{a,b\}$
- $\{a,b,c\} \cup \{d,e\} = \{a,b,c,d,e\}$

#### 11. 삼각함수, sin, cos, tan
```
$\cos (2\theta) = \cos^2 \theta - \sin^2 \theta$
```
- $\cos (2\theta) = \cos^2 \theta - \sin^2 \theta$

#### 12. 원주율 파이(pi)
```
$\pi$
$\Pi$
$\phi$
```
- $\pi$
- $\Pi$
- $\phi$

#### 13. 각도
```
$90^\circ$
```
- $90^\circ$

#### 14. 로그(log)
```
$\log_b a$
```
- $\log_b a$

#### 15. 행렬 (matrix)
```
$$A_{m,n} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n}
 \end{pmatrix}$$
```

$$A_{m,n} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n}
 \end{pmatrix}$$

#### 16. 벡터, 스칼라 (Vector, Scalar)
```
$\overrightarrow{AB}$
$\overline{AB}$
```
- $\overrightarrow{AB}$
- $\overline{AB}$

#### 17. 논문에 자주 나오는 기호
- 명령어 앞에 `\`를 붙여서 사용

##### 17-1. 특수문자
| 이름  | 명령어     | 반환 | 이름   | 명령어     | 반환 |
|-----|---------|----|------|---------|----|
| 알파  | alpha   | α  | 크사이  | xi      | ξ  |
| 베타  | beta    | β  | 오미크론 | o       | o  |
| 감마  | gamma   | γ  | 파이   | pi      | π  |
| 델타  | delta   | δ  | 로    | rho     | ρ  |
| 엡실론 | epsilon | ϵ  | 시그마  | sigma   | σ  |
| 제타  | zeta    | ζ  | 타우   | tau     | τ  |
| 에타  | eta     | η  | 입실론  | upsilon | υ  |
| 세타  | theta   | θ  | 파이   | phi     | ϕ  |
| 이오타 | iota    | ι  | 카이   | chi     | χ  |
| 카파  | kappa   | κ  | 오메가  | omega   | ω  |
| 람다  | lambda  | λ  | 뉴    | nu      | ν  |
| 뮤   | mu      | μ  |

##### 17-2. 관계연산자
| 이름        | 명령어 | 반환 | 이름        | 명령어 | 반환 |
| ----------- | ------ | ---- | ----------- | ------ | ---- |
| 합동        | equiv  | ≡    | 근사        | approx | ≈    |
| 비례        | propto | ∝    | 같고 근사   | simeq  | ≃    |
| 닮음        | sim    | ∼    | 같지 않음   | neq    | ≠    |
| 작거나 같음 | leq    | ≤    | 크거나 같음 | geq    | ≥    |
| 매우작음    | ll     | ≪    | 매우 큼     | gg     | ≫    |

##### 17-3. 논리기호
| 이름           | 명령어            | 반환 | 이름           | 명령어        | 반환 |
|--------------|----------------|----|--------------|------------|----|
| 불릿           | bullet         | ∙  | 부정           | neq        | ≠  |
| wedge        | wedge          | ∧  | vee          | vee        | ∨  |
| 논리합          | oplus          | ⊕  | 어떤           | exists     | ∃  |
| 오른쪽 </br>화살표 | rightarrow     | →  | 왼쪽 <br>화살표   | leftarrow  | ←  |
| 왼쪽 <br>큰화살표  | Leftarrow      | ⇐  | 오른쪽 <br>큰화살표 | Rightarrow | ⇒  |
| 양쪽 <br>큰화살표  | Leftrightarrow | ⇔  | 양쪽 <br>화살표   | leftarrow  | ←  |
| 모든           | forall         | ∀  |

##### 17-4. 집합기호
| 이름     | 명령어       | 반환 | 이름    | 명령어                  | 반환  |
|--------|-----------|----|-------|----------------------|-----|
| 교집합    | cap       | ∩  | 합집합   | cup                  | ∪   |
| 상위집합   | supset    | ⊃  | 진상위집합 | supseteq             | ⊇   |
| 하위집합   | subset    | ⊂  | 진하위집  | subseteq             | ⊆   |
| 부분집합아님 | notsubset | ⊄  | 공집합   | emptyset, varnothing | ∅ ∅ |
| 원소     | in        | ∈  | 원소아님  | notin                | ∉   |

##### 17-5. 기타
| 이름     | 명령어       | 반환  | 이름       | 명령어          | 반환 |
|--------|-----------|-----|----------|--------------|----|
| hat    | hat{x}    | x^  | widehat  | widehat{x}   | x^ |
| 물결     | tilde{x}  | x~  | wide물결   | widetilde{x} | x~ |
| bar    | bar{x}    | x¯  | overline | overline{x}  | x¯ |
| check  | check{x}  | xˇ  | acute    | acute{x}     | x´ |
| grave  | grave{x}  | x`  | dot      | dot{x}       | x˙ |
| ddot   | ddot{x}   | x¨  | breve    | breve{x}     | x˘ |
| vec    | vec{x}    | x→  | 델,나블라    | nabla        | ∇  |
| 수직     | perp      | ⊥   | 평행       | parallel     | ∥  |
| 부분집합아님 | notsubset | ⊄   | 공집합      | emptyset     | ∅  |
| 가운데 점  | cdot      | ⋅   | …        | dots         | …  |
| 가운데 점들 | cdots     | ⋯   | 세로점들     | vdots        | ⋮  |
| 나누기    | div       | ÷   | 물결표      | sim          | ∼  |
| 플마,마플  | `\pm`, `\mp`    | ± ∓ | 겹물결표     | approx       | ≈  |
| prime  | prime     | ′   | 무한대      | infty        | ∞  |
| 적분     | int       | ∫   | 편미분      | partial      | ∂  |
| 한칸띄어   | `x \, y`     | xy  | 두칸       | `x\;y`          | xy |
| 네칸띄어   | `x \quad y`  | xy  | 여덟칸띄어    | `x \qquad y`    | xy |


#### 18. 적분 (integral)
```
$$\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x$$

$$\int\limits_a^b$$
```

- $\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x$

- $\int\limits_a^b$


#### 19. 미분 (differential)
- 편미분
	```
	$\frac{\partial z}{\partial x}$
	```
	- $\frac{\partial z}{\partial x}$

- 그라디언트
	```
	$\nabla$
	```
	- $\nabla$


#### 20. 극한(limit)
```
$$\lim_{x \to \infty} \exp(-x) = 0$$
```

- $\lim_{x \to \infty} \exp(-x) = 0$


#### 21. 시그마(for)
```
$$\sum_{i=1}^{10} t_i$$

$$\displaystyle\sum_{i=1}^{10} t_i$$
```
- $\sum_{i=1}^{10} t_i$
- $\displaystyle\sum_{i=1}^{10} t_i$


---

- 출처: <https://khw11044.github.io/blog/blog-etc/2020-12-21-markdown-tutorial2/>
