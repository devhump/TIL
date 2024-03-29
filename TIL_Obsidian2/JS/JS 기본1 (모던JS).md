---
tags : [ModernJavaScript, JS]
---

## JS 기본1
```ad-note
- [[#자료형|자료형]]
- [[#alert, prompt, confirm을 이용한 상호작용|alert, prompt, confirm을 이용한 상호작용]]
- [[#형변환|형변환]]
- [[#기본 연산자와 수학|기본 연산자와 수학]]
- [[#비교연산자|비교연산자]]
```


#### 참고문서
##### KDT/ Web
``` dataview
list FROM "KDT/Web"
SORT file.name ASC
```
##### Modern JS
```dataview
list from #ModernJavaScript 
SORT file.name ASC
```
##### CodingApple/ JS
```dataview
list from #CodingApple/JS 
SORT file.name ASC
```



#### 스크립트 작성 방법
1. html 본문 내 script 내부에 작성한다. 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <script>
        alert("자바스크립트!")A
    </script>
</body>
</html>
```

2. 별도의 js 파일을 작성해서 불러온다
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <script src="test_js.js"></script>
</body>
</html>
```

```js
alert("에러가 발생합니다.");

[1, 2].forEach(alert)
```


#### 주석달기
```js
// 한줄 주석

/* 여러 
줄
주석 */
```


### 자료형
##### 숫자형
- 어느 수든 0으로 나누면 무한대를 얻을 수 있다. 
```js
alert( 1 / 0 ); // 무한대
alert( Infinity ); // 무한대
```

- NaN은 계산 중에 에러가 발생했다는 것을 나타내주는 값입니다. 부정확하거나 정의되지 않은 수학 연산을 사용하면 계산 중에 에러가 발생하는데, 이때 NaN이 반환됩니다.
```js
alert( "숫자가 아님" / 2 ); // NaN, 문자열을 숫자로 나누면 오류가 발생합니다.
```


##### BigInt
내부 표현 방식 때문에 자바스크립트에선 (253-1)(9007199254740991) 보다 큰 값 혹은 -(253-1) 보다 작은 정수는 '숫자형’을 사용해 나타낼 수 없습니다.
```js
// 끝에 'n'이 붙으면 BigInt형 자료입니다.
const bigInt = 1234567890123456789012345678901234567890n;
```

##### 문자열
```js
let name = "John";

// 변수를 문자열 중간에 삽입
alert( `Hello, ${name}!` ); // Hello, John!

// 표현식을 문자열 중간에 삽입
alert( `the result is ${1 + 2}` ); // the result is 3
```
- 👉 숫자 표현식도 백틱(` `` `) 내부에 표현가능

##### undefined
- undefined 값도 null 값처럼 자신만의 자료형을 형성합니다.
- undefined는 '값이 할당되지 않은 상태’를 나타낼 때 사용합니다.
- **변수는 선언했지만, 값을 할당하지 않았다면 해당 변수에 undefined가 자동**으로 할당됩니다.

```js
let age;
alert(age); // 'undefined'가 출력됩니다.

let age = 100;
// 값을 undefined로 바꿉니다.
age = undefined;
alert(age); // "undefined"
```
- 👉 변수가 ‘비어있거나’ ‘알 수 없는’ 상태라는 걸 나타내려면 null을 사용하세요. undefined는 값이 할당되지 않은 변수의 초기값을 위해 예약어로 남겨둡시다.

##### typeof
- typeof 연산자는 인수의 자료형을 반환합니다. 자료형에 따라 처리 방식을 다르게 하고 싶거나 변수의 자료형을 빠르게 알아내고자 할 때 유용합니다.
- typeof 연산자는 두 가지 형태의 문법을 지원합니다.
	1. 연산자: typeof x
	2. 함수: typeof(x)
	- 👉 괄호가 있든 없든 결과가 동일합니다.

```js
typeof undefined // "undefined"

typeof 0 // "number"

typeof 10n // "bigint"

typeof true // "boolean"

typeof "foo" // "string"

typeof Symbol("id") // "symbol"

typeof Math // "object"  (1)

typeof null // "object"  (2)

typeof alert // "function"  (3)
```
- 👉 `null`은 별도의 고유한 자료형을 가지는 특수 값으로 객체가 아니지만, 하위 호환성을 유지하기 위해 이런 오류를 수정하지 않고 남겨둔 상황입니다. 언어 자체의 오류이므로 `null`이 객체가 아님에 유의하시기 바랍니다.
- 👉 typeof는 피연산자가 함수면 "function"을 반환합니다. 그러므로 typeof alert는 "function"을 출력해줍니다. 그런데 '함수’형은 따로 없습니다. 함수는 객체형에 속합니다. 이런 동작 방식이 형식적으론 잘못되긴 했지만, 아주 오래전에 만들어진 규칙이었기 때문에 하위 호환성 유지를 위해 남겨진 상태입니다. 한편, 실무에선 이런 특징이 매우 유용하게 사용되기도 합니다.

#### 요약
- 자바스크립트에는 여덟 가지 기본 자료형이 있습니다.

```ad-tip
- 숫자형 – 정수, 부동 소수점 숫자 등의 숫자를 나타낼 때 사용합니다. 정수의 한계는 $±2^{53}$ 입니다.
- bigint – 길이 제약 없이 정수를 나타낼 수 있습니다.
- 문자형 – 빈 문자열이나 글자들로 이뤄진 문자열을 나타낼 때 사용합니다. 단일 문자를 나타내는 별도의 자료형은 없습니다.
- 불린형 – true, false를 나타낼 때 사용합니다.
- null – null 값만을 위한 독립 자료형입니다. null은 알 수 없는 값을 나타냅니다.
- undefined – undefined 값만을 위한 독립 자료형입니다. undefined는 할당되지 않은 값을 나타냅니다.
- 객체형 – 복잡한 데이터 구조를 표현할 때 사용합니다.
- 심볼형 – 객체의 고유 식별자를 만들 때 사용합니다.
```

- typeof 연산자는 피연산자의 자료형을 알려줍니다.
- typeof x 또는 typeof(x) 형태로 사용합니다.
- 피연산자의 자료형을 문자열 형태로 반환합니다.
- null의 typeof 연산은 "object"인데, 이는 언어상 오류입니다. null은 객체가 아닙니다.


### alert, prompt, confirm을 이용한 상호작용
```js
alert("Hello");

result = prompt(title, [default]);
```

#### prompt
- 브라우저에서 제공하는 prompt 함수는 두 개의 인수를 받습니다.

```js
result = prompt(title, [default]);
```
- 함수가 실행되면 텍스트 메시지와 입력 필드(input field), 확인(OK) 및 취소(Cancel) 버튼이 있는 모달 창을 띄워줍니다.

- title
	- 사용자에게 보여줄 문자열
- default
	- 입력 필드의 초깃값(선택값)

```js
let age = prompt('나이를 입력해주세요.', 100);

alert(`당신의 나이는 ${age}살 입니다.`); // 당신의 나이는 100살입니다.
```


#### confirm
```js
result = confirm(question);
```
- `confirm` 함수는 매개변수로 받은 `question(질문)`과 확인 및 취소 버튼이 있는 모달 창을 보여줍니다.
- 사용자가 확인 버튼을 누르면 `true`, 그 외의 경우는 `false`를 반환합니다.

```js
let isBoss = confirm("당신이 주인인가요?");

alert( isBoss ); // 확인 버튼을 눌렀다면 true가 출력됩니다.
```

#### 요약
- 브라우저는 사용자와 상호작용할 수 있는 세 가지 함수를 제공합니다.
- `alert`
	- 메시지를 보여줍니다.
- `prompt`
	- 사용자에게 텍스트를 입력하라는 메시지를 띄워줌과 동시에, 입력 필드를 함께 제공합니다. 확인을 누르면 `prompt` 함수는 사용자가 입력한 문자열을 반환하고, 취소 또는 Esc를 누르면 `null`을 반환합니다.
- `confirm`
	- 사용자가 확인 또는 취소 버튼을 누를 때까지 메시지가 창에 보여집니다. 사용자가 확인 버튼을 누르면 `true`를, 취소 버튼이나 Esc를 누르면 `false`를 반환합니다.

- 위 함수들은 모두 모달 창을 띄워주는데, 모달 창이 떠 있는 동안은 스크립트의 실행이 일시 중단됩니다. 사용자가 창을 닫기 전까진 나머지 페이지와 상호 작용이 불가능합니다.

- 지금까지 살펴본 세 함수엔 두 가지 제약사항이 있습니다.
1. 모달 창의 위치는 브라우저가 결정하는데, 대개 브라우저 중앙에 위치합니다.
2. 모달 창의 모양은 브라우저마다 다릅니다. 개발자는 창의 모양을 수정할 수 없습니다.

### 형변환
#### 문자형으로 변환
```js
let value = true;
alert(typeof value); // boolean

value = String(value); // 변수 value엔 문자열 "true"가 저장됩니다.
alert(typeof value); // string
```

#### 숫자형으로 변환
```js
alert( "6" / "2" ); // 3, 문자열이 숫자형으로 자동변환된 후 연산이 수행됩니다.

let str = "123";
alert(typeof str); // string

let num = Number(str); // 문자열 "123"이 숫자 123으로 변환됩니다.

alert(typeof num); // number

```

```js
let age = Number("임의의 문자열 123");

alert(age); // NaN, 형 변환이 실패합니다.
```
- 👉 숫자 이외의 글자가 들어가 있는 문자열을 숫자형으로 변환하려고 하면, 그 결과는 `NaN`이 됩니다

| 전달받은 값         | 형 변환 후                                                                                    |
|----------------|-------------------------------------------------------------------------------------------|
| undefined      | NaN                                                                                       |
| null           | 0                                                                                         |
| true and false | 1 과 0                                                                                     |
| string         | 문자열의 처음과 끝 공백이 제거됩니다. 공백 제거 후 남아있는 문자열이 없다면 0, 그렇지 않다면 문자열에서 숫자를 읽습니다. 변환에 실패하면 NaN이 됩니다. |
```js
alert( Number("   123   ") ); // 123
alert( Number("123z") );      // NaN ("z"를 숫자로 변환하는 데 실패함)
alert( Number(true) );        // 1
alert( Number(false) );       // 0
```

#### 불린형으로 변환
- 숫자 0, 빈 문자열, null, undefined, NaN과 같이 직관적으로도 “비어있다고” 느껴지는 값들은 false가 됩니다.
- 그 외의 값은 true로 변환됩니다.

```js
alert( Boolean(1) ); // 숫자 1(true)
alert( Boolean(0) ); // 숫자 0(false)

alert( Boolean("hello") ); // 문자열(true)
alert( Boolean("") ); // 빈 문자열(false)

alert( Boolean("0") ); // true
alert( Boolean(" ") ); // 공백이 있는 문자열도 비어있지 않은 문자열이기 때문에 true로 변환됩니다.

```


### 기본 연산자와 수학
- 피연산자(operand) 는 연산자가 연산을 수행하는 대상입니다. 5 * 2에는 왼쪽 피연산자 5와 오른쪽 피연산자 2, 총 두 개의 피연산자가 있습니다. '피연산자’는 '인수(argument)'라는 용어로 불리기도 합니다.

- 피연산자를 하나만 받는 연산자는 단항(unary) 연산자 라고 부릅니다. 피연산자의 부호를 뒤집는 단항 마이너스 연산자 -는 단항 연산자의 대표적인 예입니다.

```js
let x = 1;

x = -x;
alert( x ); // -1, 단항 마이너스 연산자는 부호를 뒤집습니다.


let x = 1, y = 3; alert( y - x ); // 2, 이항 마이너스 연산자는 뺄셈을 해줍니다.
```

#### 나머지 연산자 % 와 거듭제곱 연산자 `**`
```js
alert( 5 % 2 ); // 5를 2로 나눈 후의 나머지인 1을 출력
alert( 8 % 3 ); // 8을 3으로 나눈 후의 나머지인 2를 출력

alert( 2 ** 2 ); // 4  (2 * 2)
alert( 2 ** 3 ); // 8  (2 * 2 * 2)
alert( 2 ** 4 ); // 16 (2 * 2 * 2 * 2)

alert( 4 ** (1/2) ); // 2 (1/2 거듭제곱은 제곱근)
alert( 8 ** (1/3) ); // 2 (1/3 거듭제곱은 세제곱근)
```

#### 이항 연산자 '+'와 문자열 연결
```js
let s = "my" + "string";
alert(s); // mystring

alert( '1' + 2 ); // "12"
alert( 2 + '1' ); // "21"

alert(2 + 2 + '1' ); // '221'이 아니라 '41'이 출력됩니다.
```
- 👉 이처럼 이항 덧셈 연산자 `+`는 문자열 연결과 변환이라는 특별한 기능을 제공합니다. 다른 산술 연산자가 오직 숫자형의 피연산자만 다루고, 피연산자가 숫자형이 아닌 경우에 그 형을 숫자형으로 바꾸는 것과는 대조적입니다.

```js
alert( 6 - '2' ); // 4, '2'를 숫자로 바꾼 후 연산이 진행됩니다.
alert( '6' / '2' ); // 3, 두 피연산자가 숫자로 바뀐 후 연산이 진행됩니다.
```

#### 단항 연산자 +와 숫자형으로의 변환
```js
// 숫자에는 아무런 영향을 미치지 않습니다.
let x = 1;
alert( +x ); // 1

let y = -2;
alert( +y ); // -2

// 숫자형이 아닌 피연산자는 숫자형으로 변화합니다.
alert( +true ); // 1
alert( +"" );   // 0
```

```ad-tip
- 단항 덧셈 연산자의 활용
	```js
	let apples = "2";
	let oranges = "3";
	
	alert( apples + oranges ); // 23, 이항 덧셈 연산자는 문자열을 연결합니다.

	let apples = "2";
	let oranges = "3";
	
	// 이항 덧셈 연산자가 적용되기 전에, 두 피연산자는 숫자형으로 변화합니다.
	alert( +apples + +oranges ); // 5
	
	// `Number(...)`를 사용해서 같은 동작을 하는 코드를 작성할 수 있지만, 더 기네요.
	// alert( Number(apples) + Number(oranges) ); // 5
	```
	- 👉 동일한 기호의 단항 연산자는 이항 연산자보다 우선순위가 더 높디 때문에
```

#### 할당 연산자 체이닝
```js
let a, b, c;

a = b = c = 2 + 2;

alert( a ); // 4
alert( b ); // 4
alert( c ); // 4

// 하지만 되도록 아래와 같이 쓰는 것이 가독성이 더 좋
c = 2 + 2;
b = c;
a = c;
```

#### 증가·감소 연산자
- **증가(increment) 연산자** `++`는 변수를 1 증가시킵니다.
- **감소(decrement) 연산자** `--`는 변수를 1 감소시킵니다.

```js
let counter = 2;
counter++;      // counter = counter + 1과 동일하게 동작합니다. 하지만 식은 더 짧습니다.
alert( counter ); // 3

let counter = 2;
counter--;      // counter = counter - 1과 동일하게 동작합니다. 하지만 식은 더 짧습니다.
alert( counter ); // 1
```
- 👉 ==증가·감소 연산자는 변수에만 쓸 수 있습니다.== 5++와 같이 값에 사용하려고 하면 에러가 발생합니다.

 - `++`와`--` 연산자는 변수 앞이나 뒤에 올 수 있습니다. (각각 전위형, 후위형)
	 - `counter++`와 같이 피연산자 뒤에 올 때는, '후위형(postfix form)'이라고 부릅니다.
	 - `++counter`와 같이 피연산자 앞에 올 때는, '전위형(prefix form)'이라고 부릅니다.
	- 👉 ***전위형은 증가·감소 후의 새로운 값을 반환하는 반면, 후위형은 증가·감소 전의 기존 값을 반환***합니다.

```js
let counter = 1;
let a = ++counter; // (*)

alert(a); // 2

///////////////////////////////////////////////////////////

let counter = 1;
let a = counter++; // (*) ++counter를 counter++로 바꿈

alert(a); // 1
```


#### 쉼표연산자
- 코드를 짧게 쓰려는 의도로 가끔 사용됩니다.
- 쉼표 연산자 ,는 여러 표현식을 코드 한 줄에서 평가할 수 있게 해줍니다. 이때 표현식 각각이 모두 평가되지만, 마지막 표현식의 평가 결과만 반환되는 점에 유의해야 합니다.
```js
let a = (1 + 2, 3 + 4);

alert( a ); // 7 (3 + 4의 결과)
```

- 사용예시
```js
// 한 줄에서 세 개의 연산이 수행됨
for (a = 1, b = 3, c = a * b; a < 10; a++) {
 ...
}
```


### 비교연산자
#### 불린형 반환
```js
let result = 5 > 4; // 비교 결과를 변수에 할당
alert( result ); // true
```

#### 문자열 비교
```js
alert( 'Z' > 'A' ); // true
alert( 'Glow' > 'Glee' ); // true
alert( 'Bee' > 'Be' ); // true
```

- 자바스크립트는 ‘사전’ 순으로 문자열을 비교합니다. (또는 사전편집(lexicographical)순)
- 문자열 비교 시 적용되는 알고리즘은 다음과 같습니다.

1. 두 문자열의 첫 글자를 비교합니다.
2. 첫 번째 문자열의 첫 글자가 다른 문자열의 첫 글자보다 크면(작으면), 첫 번째 문자열이 두 번째 문자열보다 크다고(작다고) 결론 내고 비교를 종료합니다.
3. 두 문자열의 첫 글자가 같으면 두 번째 글자를 같은 방식으로 비교합니다.
4. 글자 간 비교가 끝날 때까지 이 과정을 반복합니다.
5. 비교가 종료되었고 문자열의 길이도 같다면 두 문자열은 동일하다고 결론 냅니다. 비교가 종료되었지만 두 문자열의 길이가 다르면 길이가 긴 문자열이 더 크다고 결론 냅니다.

#### 다른 형을 가진 값 간의 비교
- 비교하려는 값의 자료형이 다르면 자바스크립트는 이 값들을 숫자형으로 바꿉니다.
- 불린값의 경우 `true`는 `1`, `false`는 `0`으로 변환된 후 비교가 이뤄집니다.

```js
alert( '2' > 1 ); // true, 문자열 '2'가 숫자 2로 변환된 후 비교가 진행됩니다.
alert( '01' == 1 ); // true, 문자열 '01'이 숫자 1로 변환된 후 비교가 진행됩니다.

alert( true == 1 ); // true 
alert( false == 0 ); // true
```

```ad-tip
- 흥미로운 상황
	```js
	let a = 0;
	alert( Boolean(a) ); // false
	
	let b = "0";
	alert( Boolean(b) ); // true
	
	alert(a == b); // true!
	```
- 동등 비교 연산자 ==는 (예시에서 문자열 `"0"`을 숫자 `0`으로 변환시킨 것처럼) 피연산자를 숫자형으로 바꾸지만, 'Boolean’을 사용한 명시적 변환에는 다른 규칙이 사용되기 때문입니다.
```


#### 일치 연산자
- 동등 연산자(equality operator) ==은 `0`과 `false`를 구별하지 못합니다.
```javascript
alert( 0 == false ); // true
```

- 피연산자가 빈 문자열일 때도 같은 문제가 발생하죠.
```js
alert( '' == false ); // true
```

- 👉 이런 문제는 동등 연산자 == 가 형이 다른 피연산자를 비교할 때 피연산자를 숫자형으로 바꾸기 때문에 발생합니다. (빈 문자열과 `false`는 숫자형으로 변환하면 0이 되죠.)
- **일치 연산자(strict equality operator) === 를 사용하면 형 변환 없이 값을 비교할 수 있습니다.**
	- 일치 연산자는 엄격한(strict) 동등 연산자입니다. 자료형의 동등 여부까지 검사하기 때문에 피연산자 `a`와 `b`의 형이 다를 경우 `a === b`는 즉시 `false`를 반환합니다.
```js
alert( 0 === false ); // false, 피연산자의 형이 다르기 때문입니다.
```
- 👉 일치 연산자 === 가 동등 연산자 == 의 엄격한 버전인 것처럼 ‘불일치’ 연산자 `!==`는 부등 연산자 `!=`의 엄격한 버전입니다.


#### [null이나 undefined와 비교하기](https://ko.javascript.info/comparison#ref-453)

- `null`이나 `undefined`를 다른 값과 비교할 땐 예상치 않은 일들이 발생합니다. 일단 몇 가지 규칙을 먼저 살펴본 후, 어떤 예상치 않은 일들이 일어나는지 구체적인 예시를 통해 살펴보도록 하겠습니다.

- 일치 연산자 === 를 사용하여 `null`과 `undefined`를 비교
	- 두 값의 자료형이 다르기 때문에 일치 비교 시 거짓이 반환됩니다.

```js
alert( null === undefined ); // false`
```

- 동등 연산자 == 를 사용하여 `null`과 `undefined`를 비교
	- 동등 연산자를 사용해 `null`과 `undefined`를 비교하면 특별한 규칙이 적용돼 `true`가 반환됩니다. 동등 연산자는 `null`과 `undefined`를 '각별한 커플’처럼 취급합니다. 두 값은 자기들끼리는 잘 어울리지만 다른 값들과는 잘 어울리지 못합니다.
```js
alert( null == undefined ); // true`
```

- 산술 연산자나 기타 비교 연산자 `<`, `>`, `<=`, `>=`를 사용하여 `null`과 `undefined`를 비교
	- `null`과 `undefined`는 숫자형으로 변환됩니다. `null`은 `0`, `undefined`는 `NaN`으로 변합니다.

##### null vs 0
- null과 0을 비교해 봅시다.
```js
alert( null > 0 );  // (1) false
alert( null == 0 ); // (2) false
alert( null >= 0 ); // (3) true
```
- 위 비교 결과는 논리에 맞지 않아 보입니다. (3)에서 null은 0보다 크거나 같다고 했기 때문에, (1)이나 (2) 중 하나는 참이어야 하는데 둘 다 거짓을 반환하고 있네요.

- 이런 결과가 나타나는 이유는 동등 연산자 == 와 기타 비교 연산자 <, >, <=, >=의 동작 방식이 다르기 때문입니다. (1)에서 null > 0이 거짓을, (3)에서 null >= 0이 참을 반환하는 이유는 (기타 비교 연산자의 동작 원리에 따라) null이 숫자형으로 변환돼 0이 되기 때문입니다.

- 그런데 동등 연산자 == 는 피연산자가 undefined나 null일 때 형 변환을 하지 않습니다. undefined와 null을 비교하는 경우에만 true를 반환하고, 그 이외의 경우(null이나 undefined를 다른 값과 비교할 때)는 무조건 false를 반환합니다. 이런 이유 때문에 (2)는 거짓을 반환합니다.

##### 비교가 불가능한 undefined
- undefined를 다른 값과 비교해서는 안 됩니다.
```js
alert( undefined > 0 ); // false (1)
alert( undefined < 0 ); // false (2)
alert( undefined == 0 ); // false (3)
```
- 위 예시를 보면 undefined는 0을 매우 싫어하는 것처럼 보입니다. 항상 false를 반환하고 있네요.

- 이런 결과는 아래와 같은 이유 때문에 발생합니다.

- (1)과(2)에선 undefined가 NaN으로 변환되는데(숫자형으로의 변환), NaN이 피연산자인 경우 비교 연산자는 항상 false를 반환합니다.
- undefined는 null이나 undefined와 같고, 그 이외의 값과는 같지 않기 때문에 (3)은 false를 반환합니다.

#### 함정 피하기
- 위와 같은 에지 케이스를 왜 살펴보았을까요? 이런 예외적인 경우를 꼭 기억해 놓고 있어야만 할까요? 그렇지는 않습니다. 개발을 하다 보면 자연스레 이런 경우를 만나고 점차 익숙해지기 때문에 지금 당장 암기해야 할 필요는 없습니다. 하지만 아래와 같은 방법을 사용해 이런 예외 상황을 미리 예방할 수 있다는 점은 알아두시길 바랍니다.

- 일치 연산자 === 를 제외한 비교 연산자의 피연산자에 undefined나 null이 오지 않도록 특별히 주의하시기 바랍니다.
- 또한, undefined나 null이 될 가능성이 있는 변수가 <, >, <=, >=의 피연산자가 되지 않도록 주의하시기 바랍니다. 명확한 의도를 갖고 있지 않은 이상 말이죠. 만약 변수가 undefined나 null이 될 가능성이 있다고 판단되면, 이를 따로 처리하는 코드를 추가하시기 바랍니다.

##### 요약
- 비교 연산자는 불린값을 반환합니다.
- 문자열은 문자 단위로 비교되는데, 이때 비교 기준은 ‘사전’ 순입니다.
- 서로 다른 타입의 값을 비교할 땐 숫자형으로 형 변환이 이뤄지고 난 후 비교가 진행됩니다(일치 연산자는 제외).
- null과 undefined는 동등 비교(== ) 시 서로 같지만 다른 값과는 같지 않습니다.
- null이나 undefined가 될 확률이 있는 변수가 > 또는 <의 피연산자로 올 때는 주의를 기울이시기 바랍니다. null, undefined 여부를 확인하는 코드를 따로 추가하는 습관을 들이길 권유합니다