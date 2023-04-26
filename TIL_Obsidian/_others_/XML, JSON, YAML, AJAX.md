### XML vs JSON
컴퓨터 간에 정보를 주고 받기 위해서는 계층과 구조를 가진 정보를 텍스트로 표현할 수 있는 형식이 필요한데, 대표적인 것이 XML과 JSON이다.

#### XML
- [MS - 초보자를 위한 XML 설명](https://support.microsoft.com/ko-kr/office/%EC%B4%88%EB%B3%B4%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-xml-%EC%84%A4%EB%AA%85-a87d234d-4c2e-4409-9cbc-45e4eb857d44)
- xml 예시
```xml
<?xml version="1.0"?>
<CAT>
  <NAME>Izzy</NAME>
  <BREED>Siamese</BREED>
  <AGE>6</AGE>
  <ALTERED>yes</ALTERED>
  <DECLAWED>no</DECLAWED>
  <LICENSE>Izz138bod</LICENSE>
  <OWNER>Colin Wilcox</OWNER>
</CAT>
```

> **XML**(eXtensible Markup Language)은 [W3C](https://ko.wikipedia.org/wiki/W3C "W3C")에서 개발된, 다른 특수한 목적을 갖는 [마크업 언어](https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EC%97%85_%EC%96%B8%EC%96%B4 "마크업 언어")를 만드는데 사용하도록 권장하는 **다목적 [마크업 언어](https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EC%97%85_%EC%96%B8%EC%96%B4 "마크업 언어")이다.** XML은 [SGML](https://ko.wikipedia.org/wiki/SGML "SGML")의 단순화된 부분집합으로, 다른 많은 종류의 데이터를 기술하는 데 사용할 수 있다. XML은 주로 다른 종류의 시스템, <u>특히 [인터넷](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%EB%84%B7 "인터넷")에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게 하여 [HTML](https://ko.wikipedia.org/wiki/HTML "HTML")의 한계를 극복할 목적</u>으로 만들어졌다.
> 
> \-by 위키피디아, [XML 에 관한 설명](https://ko.wikipedia.org/wiki/XML)

- 👉 플랫폼 간에 데이터를 주고 받기 위해 특화된, **마크업 언어**이며 HTML처럼 여는 태그-닫는 태그들의 계층으로 구성되어 있다.

#### JSON
- XML에서 사용하는 태그는 각 항목의 내용이 시작되는 곳과 끝나는 곳을 표시함으로써 데이터의 구조를 명확히 보여준다. 다만 반복되는 텍스트가 많아 전체 길이가 길어지는 단점이 있다. 이를 보완한 것이 **JSON**이다.

> **JSON**(**제이슨**[[1]](https://ko.wikipedia.org/wiki/JSON#cite_note-Pronunciation-1), JavaScript Object Notation)은 [속성-값 쌍](https://ko.wikipedia.org/w/index.php?title=%EC%86%8D%EC%84%B1-%EA%B0%92_%EC%8C%8D&action=edit&redlink=1 "속성-값 쌍 (없는 문서)")(attribute–value pairs), 배열 자료형(array data types) 또는 기타 모든 시리얼화 가능한 값(serializable value) 또는 "키-값 쌍"으로 이루어진 데이터 오브젝트를 전달하기 위해 인간이 읽을 수 있는 텍스트를 사용하는 [개방형 표준](https://ko.wikipedia.org/wiki/%EA%B0%9C%EB%B0%A9%ED%98%95_%ED%91%9C%EC%A4%80 "개방형 표준") 포맷이다.
> 
> \-by 위키피디아, [JSON에 관한 설명](https://ko.wikipedia.org/wiki/JSON)

- [Oracle - JSON이란 무엇인가?](https://www.oracle.com/kr/database/what-is-json/)
- [MDN - # JSON으로 작업하기](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/JSON)

##### JSON 구조
- JSON은 Javascript 객체 리터럴 문법을 따르는 문자열. 
- JSON 안에는 마찬가지로 Javascript의 기본 데이터 타입인 문자열, 숫자, 배열, 불리언 그리고 다른 객체를 포함할 수 있다. 

```json
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```


### YAML

> - **YAML**은 [XML](https://ko.wikipedia.org/wiki/XML "XML"), [C](https://ko.wikipedia.org/wiki/C_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4) "C (프로그래밍 언어)"), [파이썬](https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC "파이썬"), [펄](https://ko.wikipedia.org/wiki/%ED%8E%84 "펄"), [RFC2822](https://ko.wikipedia.org/w/index.php?title=RFC2822&action=edit&redlink=1 "RFC2822 (없는 문서)")에서 정의된 e-mail 양식에서 개념을 얻어 만들어진 '사람이 쉽게 읽을 수 있는' 데이터 직렬화 양식이다. 2001년에 [클라크 에반스](https://ko.wikipedia.org/w/index.php?title=%ED%81%B4%EB%9D%BC%ED%81%AC_%EC%97%90%EB%B0%98%EC%8A%A4&action=edit&redlink=1 "클라크 에반스 (없는 문서)")가 고안했고, Ingy dot Net 및 Oren Ben-Kiki와 함께 디자인했다.
>- YAML이라는 이름은 "YAML은 마크업 언어가 아니다 (YAML Ain't Markup Language)” 라는 [재귀적인 이름](https://ko.wikipedia.org/wiki/%EC%9E%AC%EA%B7%80_%EC%95%BD%EC%9E%90 "재귀 약자")에서 유래되었다.
>
>\-by 위키피디아, [YAML](https://ko.wikipedia.org/wiki/YAML)

- [RedHat - YAML이란?](https://www.redhat.com/ko/topics/automation/what-is-yaml)
- 주로 프로그램 설정 파일과 같이 개발자가 편리하게 읽고 작성하기 위한 용도로 사용됨
	- (↔ XML, JSON은 프로그램 간 정보 전달이 주목적)
- 정보인식을 위해 줄바꿈과 들여쓰기가 필수 문법 요소

```yaml
name: 얄코치킨
location: 한빛시 얄코구 혼공로 열공길
owner: 
	name: 김얄코
	phone: 010-1234-5678
meuns:
	- name: 매콤치킨
		price : 18000
		ingredient:
		- 닭
		- 튀김가루
		- 핫소스
	2:
	- name: 핫윙
		price : 10000
		ingredient:
		- 닭날개
		- 핫소스
```


### AJAX
- AJAX(에이젝스)는 정확히는 형식이 아니다. AJAX는 자바스크립트를 이용해 서버와 브라우저가 데이터를 교환할 수 있는 통신 기능을 한다. 
- AJAX는 Asynchronous JavaScript And XML의 약자로, 이름 그대로 자바스크립트를 통해서 서버에 비동기 방식으로 요청하는 것을 의미한다. 

### 참고문헌
- 위키피디아 단어의 정의
- <혼자 공부하는 얄팍한 코딩지식> by 고현민, 한빛미디어