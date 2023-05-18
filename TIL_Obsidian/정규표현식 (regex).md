
### 참고 내용 및 자료
- [Youtube -정규표현식 , 더이상 미루지 말자 🤩 by 드림코딩](https://youtu.be/t3M6toIflyQ)
	- [정규 표현식 정리 - 드림코딩 (github)](https://github.com/dream-ellie/regex)
	- [정규표현식 연습 사이트](https://regexr.com/5mhou)
	- [Regexone (퀴즈)](https://regexone.com/)
- 추가 👉 [+a 내용이 잘 정리 된 블로그 / 정규표현식 in python](https://nachwon.github.io/regular-expressions/)

### 문법 정리
#### Groups and ranges
| Character | 뜻                                     |
| :--------: | -------------------------------------- |
| `\|`      | 또는                                   |
| `()`      | 그룹                                   |
| `[]`      | 문자셋, 괄호안의 어떤 문자든           |
| `[^]`     | 부정 문자셋, 괄호안의 어떤 문가 아닐때 |
| `(?:)`    | 찾지만 기억하지는 않음                 |

#### Quantifiers
| Character   | 뜻                                  |
| :-----------: | ----------------------------------- |
| `?`         | 없거나 있거나 (zero or one)         |
| `*`         | 없거나 있거나 많거나 (zero or more) |
| `+`         | 하나 또는 많이 (one or more)        |
| `{n}`       | n번 반복                            |
| `{min,}`    | 최소                                |
| `{min,max}` | 최소, 그리고 최대                   |

#### Boundary-type
| Character | 뜻               |
| :--------: | ---------------- |
| `\b`      | 단어 경계        |
| `\B`      | 단어 경계가 아님 |
| `^`       | 문장의 시작      |
| `$`       | 문장의 끝        |

#### Character classes
| Character | 뜻                           |
| :-------: | ---------------------------- |
| `\`       | 특수 문자가 아닌 문자        |
| `.`       | 어떤 글자 (줄바꿈 문자 제외) |
| `\d`      | digit 숫자                   |
| `\D`      | digit 숫자 아님              |
| `\w`      | word 문자                    |
| `\W`      | word 문자 아님               |
| `\s`      | space 공백                   |
| `\S`      | space 공백 아님              |

### 예제
```ad-question
- Q1. 전화번호 찾기 정규 표현식은?
	- 02-123-4567
	- 010.1234.5678
	- 080 8888 9999
- Q2. 이메일을 찾기 위한 정규표현식은?
- Q3. 유튜브 북마크 주소를 찾기 위한 정규표현식은?
```

```regex
Q1. 
\d{2,3}[- .]\d{3}[- .]\d{4}

Q2.
[a-zA-Z0-9._+-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9.]+


Q3.
(https?:\/\/)?(www\.)?youtu.be\/([a-zA-Z0-9-]{11})
또는
(?:https?:\/\/)?(?:www\.)?youtu.be\/([a-zA-Z0-9-]{11})
```

#### `?:`의 유무에 따른 차이
![](assets/정규표현식%20(regex)-1.png)

![](assets/정규표현식%20(regex).png)

### 실 사용 예시 (feat. JS)
![](assets/정규표현식%20(regex)-2.png)

![](assets/정규표현식%20(regex)-3.png)