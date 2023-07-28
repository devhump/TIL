---
title : 
aliases : 
tags : [ModernJavaScript, JS, syntax]
---


### 함수

#### 함수 선언
- _함수 선언(function declaration)_ 방식
```js
function showMessage() {
  alert( '안녕하세요!' );
}

// 매개변수가 많은 함수의 경
function name(parameter1, parameter2, ... parameterN) {
  // 함수 본문
}

// 함수 호출
showMessage();
showMessage();

```


##### 지역변수
- 함수 내에서 선언한 변수인 지역 변수(local variable)는 함수 안에서만 접근할 수 있습니다.
```js
function showMessage() {
  let message = "안녕하세요!"; // 지역 변수

  alert( message );
}

showMessage(); // 안녕하세요!

alert( message ); // ReferenceError: message is not defined (message는 함수 내 지역 변수이기 때문에 에러가 발생합니다.)
```

##### 외부변수
- 함수 내부에서 함수 외부의 변수인 외부 변수(outer variable)에 접근할 수 있습니다.
```js
let userName = 'John';

function showMessage() {
  let message = 'Hello, ' + userName;
  alert(message);
}

showMessage(); // Hello, John
```

- 함수에선 외부 변수에 접근하는 것뿐만 아니라, 수정도 할 수 있습니다.
```js
let userName = 'John';

function showMessage() {
  userName = "Bob"; // (1) 외부 변수를 수정함

  let message = 'Hello, ' + userName;
  alert(message);
}

alert( userName ); // 함수 호출 전이므로 John 이 출력됨

showMessage();

alert( userName ); // 함수에 의해 Bob 으로 값이 바뀜
```

```ad-tip
- **외부 변수는 지역 변수가 없는 경우에만 사용**할 수 있습니다.
- 함수 내부에 외부 변수와 동일한 이름을 가진 변수가 선언되었다면, 내부 변수는 외부 변수를 _가립니다_. 예시를 살펴봅시다. 함수 내부에 외부 변수와 동일한 이름을 가진 지역 변수 `userName`가 선언되어 있습니다. 외부 변수는 내부 변수에 가려져 값이 수정되지 않았습니다.

	```js
	let userName = 'John';
	
	function showMessage() {
	  let userName = "Bob"; // 같은 이름을 가진 지역 변수를 선언합니다.
	
	  let message = 'Hello, ' + userName; // Bob
	  alert(message);
	}
	
	// 함수는 내부 변수인 userName만 사용합니다,
	showMessage();
	
	alert( userName ); // 함수는 외부 변수에 접근하지 않습니다. 따라서 값이 변경되지 않고, John이 출력됩니다.
	```

- ***전역 변수***
	- 위 예시의 `userName`처럼, 함수 외부에 선언된 변수는 _전역 변수(global variable)_ 라고 부릅니다.
	- 전역 변수는 같은 이름을 가진 지역 변수에 의해 가려지지만 않는다면 모든 함수에서 접근할 수 있습니다.
	- 변수는 연관되는 함수 내에 선언하고, ==전역 변수는 되도록 사용하지 않는 것이 좋습니다.== 비교적 근래에 작성된 코드들은 대부분 전역변수를 사용하지 않거나 최소한으로만 사용합니다. 다만 프로젝트 전반에서 사용되는 데이터는 전역 변수에 저장하는 것이 유용한 경우도 있으니 이 점을 알아두시기 바랍니다.
```


#### 매개변수
- 매개변수(parameter)를 이용하면 임의의 데이터를 함수 안에 전달할 수 있습니다.
- 매개변수는 _인자(parameter)_ 라고 불리기도 합니다.
- 아래 예시에서 함수 showMessage는 매개변수 `from` 과 `text`를 가집니다.

```js
function showMessage(from, text) { // 인자: from, text
  alert(from + ': ' + text);
}

showMessage('Ann', 'Hello!'); // Ann: Hello! (*)
showMessage('Ann', "What's up?"); // Ann: What's up? (**)
```

- 함수의 매개변수에 전달된 값을 *인수(argument)* 라고 부르기도 합니다.
- ***매개변수***는 함수 선언 방식 괄호 사이에 있는 변수입니다(선언 시 쓰이는 용어).
- ***인수***는 함수를 호출할 때 매개변수에 전달되는 값입니다(호출 시 쓰이는 용어).

#### 기본값
- 함수 호출 시 매개변수에 인수를 전달하지 않으면 그 값은 `undefined`가 됩니다.
- 예시를 통해 이에 대해 알아봅시다. 위에서 정의한 함수 `showMessage(from, text)`는 매개변수가 2개지만, 아래와 같이 인수를 하나만 넣어서 호출할 수 있습니다.
```js
showMessage("Ann");
```

- 이렇게 코드를 작성해도 에러가 발생하지 않습니다. 두 번째 매개변수에 값을 전달하지 않았기 때문에 `text`엔 `undefined`가 할당될 뿐입니다. 따라서 에러 없이 `"Ann: undefined"`가 출력됩니다.

- 매개변수에 값을 전달하지 않아도 그 값이 `undefined`가 되지 않게 하려면 함수를 선언할 때 = 를 사용해 '기본값(default value)'을 설정해주면 됩니다.

```js
function showMessage(from, text = "no text given") {
  alert( from + ": " + text );
}

showMessage("Ann"); // Ann: no text given
```

```js
// 매개변수에 값을 전달해도 그 값이 `undefined`와 엄격히 일치한다면 기본값이 할당됩니다.
showMessage("Ann", undefined); // Ann: no text given

// 아래와 같이 복잡한 표현식도 기본값으로 설정할 수도 있습니다.
function showMessage(from, text = anotherFunction()) {
  // anotherFunction()은 text값이 없을 때만 호출됨
  // anotherFunction()의 반환 값이 text의 값이 됨
}
```

```ad-tip
- 매개변수 기본값 평가 시점

	- 자바스크립트에선 함수를 호출할 때마다 매개변수 기본값을 평가합니다. 물론 해당하는 매개변수가 없을 때만 기본값을 평가하죠.
	
	- 위 예시에선 매개변수 `text`에 값이 전달되는 경우 `anotherFunction()`은 호출되지 않습니다.
	
	- 반면 `text`에 값이 없는 경우 `showMessage()`를 호출할 때마다 `anotherFunction()`이 호출됩니다.
```


##### 구식 자바스크립트에서 매개 변수 기본값 설정하는 방법
1. 구식 코드에서는 매개변수 기본값 설정을 위해 먼저 매개변수 값이 `undefined`인지 명시적으로 확인하고, 일치하는 경우엔 기본값을 설정합니다.

```js
function showMessage(from, text) {
  if (text === undefined) {
    text = 'no text given';
  }

  alert( from + ": " + text );
}
```

2. 이 방법 말고도 논리 연산자 `||`를 사용해 매개변수 기본값을 설정하는 방법도 있습니다.
`
```js
function showMessage(from, text) {
  // text의 값이 falsy면 기본값이 할당됨
  // 이 방식은 text == ""일 경우, text에 값이 전달되지 않은것과 같다고 간주합니다..
  text = text || 'no text given';
  ...
}
```

##### 매개변수 기본값을 설정할 수 있는 또 다른 방법
```js
// case 1
function showMessage(text) {
  // ...

  if (text === undefined) { // 매개변수가 생략되었다면
    text = '빈 문자열';
  }

  alert(text);
}

showMessage(); // 빈 문자열


// case 2
// 매개변수가 생략되었거나 빈 문자열("")이 넘어오면 변수에 '빈 문자열'이 할당됩니다.
function showMessage(text) {
  text = text || '빈 문자열';
  ...
}


// case 3 
// 이 외에도 모던 자바스크립트 엔진이 지원하는 nullish 병합 연산자(nullish coalescing operator) ??를 사용하면 0처럼 falsy로 평가되는 값들을 일반 값처럼 처리할 수 있어서 좋습니다.

// 매개변수 'count'가 `undefined` 또는 `null`이면 'unknown'을 출력해주는 함수
function showCount(count) {
  alert(count ?? "unknown");
}

showCount(0); // 0
showCount(null); // unknown
showCount(); // unknown
```

#### 반환값
- 함수를 호출했을 때 함수를 호출한 그곳에 특정 값을 반환하게 할 수 있습니다. 이때 이 특정 값을 ***반환 값(return value)*** 이라고 부릅니다.
```js
function sum(a, b) {
  return a + b;
}

let result = sum(1, 2);
alert( result ); // 3
```


```ad-tip
- `return`문이 없거나 `return` 지시자만 있는 함수는 `undefined`를 반환합니다.
	```js
	function doNothing() { /* empty */ }

	alert( doNothing() === undefined ); // true
	```
- `return` 지시자만 있는 경우도 `undefined`를 반환합니다. `return`은 `return undefined`와 동일하게 동작하죠.
	```js
	function doNothing() {
	  return;
	}
	
	alert( doNothing() === undefined ); // true
	```
```

```ad-attention
- `return`과 값 사이에 절대 줄을 삽입하지 마세요.
	```js
	return 
		(some + long + expression + or + whatever * f(a) + f(b))
	
	// 위 문장은 아래와 같이 해석됩니다. 
	return; 
		(some + long + expression + or + whatever * f(a) + f(b))

	// 이를 피하기 위해선 
	return (
	  some + long + expression
	  + or +
	  whatever * f(a) + f(b)
	  )
	// 이처럼 작성해야 합니다.
	```
```


#### 함수 이름짓기
- 함수는 어떤 `동작`을 수행하기 위한 코드를 모아놓은 것입니다. 따라서 함수의 이름은 대개 동사입니다. 함수 이름은 가능한 한 간결하고 명확해야 합니다. 함수가 어떤 동작을 하는지 설명할 수 있어야 하죠. 코드를 읽는 사람은 함수 이름만 보고도 함수가 어떤 기능을 하는지 힌트를 얻을 수 있어야 합니다.

- ***이름만 보고도 어떤 동작을 하는지 알 수 있는 코드를 _자기 설명적(self-describing)_ 코드가 가독성 면에서 더 좋다.***
- 함수명 짓기에 쓰이는 접두어 예시
	- `"get…"` – 값을 반환함
	- `"calc…"` – 무언가를 계산함
	- `"create…"` – 무언가를 생성함
	- `"check…"` – 무언가를 확인하고 불린값을 반환함

```ad-tip
- 함수는 ==동작 하나만 담당==해야 합니다.

- 함수는 함수 이름에 언급되어 있는 동작을 정확히 수행해야 합니다. 그 이외의 동작은 수행해선 안 됩니다.

- 독립적인 두 개의 동작은 독립된 함수 두 개에서 나눠서 수행할 수 있게 해야 합니다. 한 장소에서 두 동작을 동시에 필요로 하는 경우라도 말이죠(이 경우는 제3의 함수를 만들어 그곳에서 두 함수를 호출합니다).
```

#### 요약
- 함수 선언 방식으로 함수를 만들 수 있습니다.
```js
function 함수이름(복수의, 매개변수는, 콤마로, 구분합니다) {
  /* 함수 본문 */
}
```

- 함수(function)
	- 함수에 전달된 매개변수는 복사된 후 함수의 지역변수가 됩니다.
	- 함수는 외부 변수에 접근할 수 있습니다. 하지만 함수 바깥에서 함수 내부의 지역변수에 접근하는 건 불가능합니다.
	- 함수는 값을 반환할 수 있습니다. 값을 반환하지 않는 경우는 반환 값이 undefined가 됩니다.

- 깔끔하고 이해하기 쉬운 코드를 작성하려면 함수 내부에서 외부 변수를 사용하는 방법 대신 지역 변수와 매개변수를 활용하는 게 좋습니다.

- 개발자는 매개변수를 받아서 그 변수를 가지고 반환 값을 만들어 내는 함수를 더 쉽게 이해할 수 있습니다. 매개변수 없이 함수 내부에서 외부 변수를 수정해 반환 값을 만들어 내는 함수는 쉽게 이해하기 힘듭니다.

- 함수 이름을 지을 땐 아래와 같은 규칙을 따르는 것이 좋습니다.
	- 함수 이름은 함수가 어떤 동작을 하는지 설명할 수 있어야 합니다. 이렇게 이름을 지으면 함수 호출 코드만 보아도 해당 함수가 무엇을 하고 어떤 값을 반환할지 바로 알 수 있습니다.
	- 함수는 동작을 수행하기 때문에 이름이 주로 동사입니다.
	- create…, show…, get…, check… 등의 잘 알려진 접두어를 사용해 이름을 지을 수 있습니다. 접두어를 사용하면 함수 이름만 보고도 해당 함수가 어떤 동작을 하는지 파악할 수 있습니다.

- 함수는 스크립트를 구성하는 주요 구성 요소입니다. 지금까지 다룬 내용은 함수의 기본입니다. 여기선 함수를 만드는 방법, 사용하는 방법을 소개했는데 이 내용은 시작일 뿐입니다. 이어지는 챕터에선 지금까지 배운 것을 바탕으로 함수가 제공하는 고급 기능에 대해 학습해 보도록 하겠습니다.

---

### 함수 표현식
- 자바스크립트는 함수를 특별한 종류의 값으로 취급합니다. 다른 언어에서처럼 "특별한 동작을 하는 구조"로 취급되지 않습니다.

- 함수 선언(Function Decalaration) 방식
```js
function sayHi() {
  alert( "Hello" );
}
```

- _함수 표현식(Function Expression)_ 방식
```js
let sayHi = function() {
  alert( "Hello" );
};
```
- 함수를 생성하고 변수에 값을 할당하는 것처럼 함수가 변수에 할당되었습니다. 함수가 어떤 방식으로 만들어졌는지에 관계없이 함수는 값이고, 따라서 변수에 할당할 수 있습니다. 위 예시에선 함수가 변수 `sayHi`에 저장된 값이 되었습니다.
	- 👉 “함수를 만들고 그 함수를 변수 `sayHi`에 할당하기”

- 👇 함수는 값이기 때문에 `alert`를 이용하여 함수 코드를 출력할 수도 있습니다.

```js
function sayHi() {
  alert( "Hello" );
}

alert( sayHi ); // 함수 코드가 보임
```
![](assets/JS%20기본3.png)
- 👆 위 코드에선 함수 소스 코드가 문자형으로 바뀌어 출력
- 마지막 줄에서 `sayHi`옆에 괄호가 없기 때문에 함수는 실행되지 않습니다. 

- ==본질은 값이기 때문에 값에 할 수 있는 일을 함수에도 할 수 있습니다.==

- 변수를 복사해 다른 변수에 할당하는 것처럼 함수를 복사해 다른 변수에 할당할 수도 있습니다.

```js
function sayHi() {   // (1) 함수 생성
  alert( "Hello" );
}

let func = sayHi;    // (2) 함수 복사

func(); // Hello     // (3) 복사한 함수를 실행(정상적으로 실행됩니다)!
sayHi(); // Hello    //     본래 함수도 정상적으로 실행됩니다.
```

- 위 문장과 아래 문장은 동일한 동작 결과를 나타냄
```js
let sayHi = function() {
  alert( "Hello" ); 
};

let func = sayHi;
// ...
```


#### 콜백 함수
- 함수를 값처럼 전달하는 예시, 함수 표현식에 관한 예시를 좀 더 살펴보겠습니다.
- 매개변수가 3개 있는 함수, `ask(question, yes, no)`를 작성해보겠습니다. 각 매개변수에 대한 설명은 아래와 같습니다.
	- `question` : 질문
	- `yes` : "Yes"라고 답한 경우 실행되는 함수
	- `no` : "No"라고 답한 경우 실행되는 함수

- 함수는 반드시 `question(질문)`을 해야 하고, 사용자의 답변에 따라 `yes()` 나 `no()`를 호출합니다.
```js
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}

function showOk() {
  alert( "동의하셨습니다." );
}

function showCancel() {
  alert( "취소 버튼을 누르셨습니다." );
}

// 사용법: 함수 showOk와 showCancel가 ask 함수의 인수로 전달됨
ask("동의하십니까?", showOk, showCancel);
```
- 👆 이때, **함수 `ask`의 인수, `showOk`와 `showCancel`은 _콜백 함수_ 또는 _콜백_이라고 불립니다.**

- ***함수를 함수의 인수로 전달하고, 필요하다면 인수로 전달한 그 함수를 "나중에 호출(called back)"하는 것이 콜백 함수의 개념***입니다. 위 예시에선 사용자가 "yes"라고 대답한 경우 `showOk`가 콜백이 되고, "no"라고 대답한 경우 `showCancel`가 콜백이 됩니다.

- 👇 함수표현식을 사용하여 코드를 더 간결하게 정리한 예시 
```js
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}

ask(
  "동의하십니까?",
  function() { alert("동의하셨습니다."); },
  function() { alert("취소 버튼을 누르셨습니다."); }
);
```

 - 👉 `ask(...)` 안에 함수가 선언된 게 보이시나요? 이렇게 이름 없이 선언한 함수는 _익명 함수(anonymous function)_ 라고 부릅니다. 익명 함수는 (변수에 할당된 게 아니기 때문에) `ask` 바깥에선 접근할 수 없습니다.

```ad-tip
- 함수는 "동작"을 나타내는 값입니다.

- 문자열이나 숫자 등의 일반적인 값들은 _데이터_를 나타냅니다.

- 함수는 하나의 *동작(action)*을 나타냅니다.

- 동작을 대변하는 값인 함수를 변수 간 전달하고, 동작이 필요할 때 이 값을 실행할 수 있습니다.
```


#### 함수 표현식 vs 함수 선언문
- 함수 표현식과 선언문의 차이에 대해 알아봅시다.

1. ==첫 번째는 문법==입니다. 코드를 통해 어떤 차이가 있는지 살펴봅시다.

- _함수 선언문:_ 함수는 주요 코드 흐름 중간에 독자적인 구문 형태로 존재합니다.
```js
// 함수 선언문 
function sum(a, b) {   
	return a + b; 
}
``` 

- _함수 표현식:_ 함수는 표현식이나 구문 구성(syntax construct) 내부에 생성됩니다. 아래 예시에선 함수가 할당 연산자 =를 이용해 만든 “할당 표현식” 우측에 생성되었습니다.
```js
// 함수 표현식 
let sum = function(a, b) {   
	return a + b; 
};
```

2. 두 번째 차이는 ==자바스크립트 엔진이 _언제_ 함수를 생성하는지==에 있습니다.

- 함수 표현식은 ***실제 실행 흐름이 해당 함수에 도달했을 때 함수를 생성합니다. 따라서 실행 흐름이 함수에 도달했을 때부터 해당 함수를 사용할 수 있습니다.***
	- 위 예시를 이용해 설명해 보도록 하겠습니다. 스크립트가 실행되고, 실행 흐름이 let sum = function…의 우측(함수 표현식)에 도달 했을때 함수가 생성됩니다. 이때 이후부터 해당 함수를 사용(할당, 호출 등)할 수 있습니다.

- 하지만 함수 선언문은 조금 다릅니다. ***함수 선언문은 함수 선언문이 정의되기 전에도 호출할 수 있습니다. 따라서 전역 함수 선언문은 스크립트 어디에 있느냐에 상관없이 어디에서든 사용할 수 있습니다.***
	- 이게 가능한 이유는 자바스크립트의 내부 알고리즘 때문입니다. 자바스크립트는 스크립트를 실행하기 전, 준비단계에서 전역에 선언된 함수 선언문을 찾고, 해당 함수를 생성합니다. 스크립트가 진짜 실행되기 전 "초기화 단계"에서 함수 선언 방식으로 정의한 함수가 생성되는 것이죠.

- ==스크립트는 함수 선언문이 모두 처리된 이후에서야 실행됩니다. 따라서 스크립트 어디서든 함수 선언문으로 선언한 함수에 접근할 수 있는 것입니다.==

3. ==세 번째 차이점은, 스코프==입니다.
- **엄격 모드에서 함수 선언문이 코드 블록 내에 위치하면 해당 함수는 블록 내 어디서든 접근할 수 있습니다. 하지만 블록 밖에서는 함수에 접근하지 못합니다.**

```js
let age = prompt("나이를 알려주세요.", 18);

// 조건에 따라 함수를 선언함
if (age < 18) {

  function welcome() {
    alert("안녕!");
  }

} else {

  function welcome() {
    alert("안녕하세요!");
  }

}

// 함수를 나중에 호출합니다.
welcome(); // Error: welcome is not defined
```

- 👉 함수 선언문은 함수가 선언된 코드 블록 안에서만 유효하기 때문에 이런 에러가 발생합니다.

```js
let age = 16; // 16을 저장했다 가정합시다.

if (age < 18) {
  welcome();               // \   (실행)
                           //  |
  function welcome() {     //  |
    alert("안녕!");        //  |  함수 선언문은 함수가 선언된 블록 내
  }                        //  |  어디에서든 유효합니다
                           //  |
  welcome();               // /   (실행)

} else {

  function welcome() {
    alert("안녕하세요!");
  }
}

// 여기는 중괄호 밖이기 때문에
// 중괄호 안에서 선언한 함수 선언문은 호출할 수 없습니다.

welcome(); // Error: welcome is not defined
```

- 반면 함수 표현식을 사용하면 `if`문 밖에서 `welcome` 함수를 호출할 수 있다. 

```js
// case 1

let age = prompt("나이를 알려주세요.", 18);

let welcome;

if (age < 18) {

  welcome = function() {
    alert("안녕!");
  };

} else {

  welcome = function() {
    alert("안녕하세요!");
  };

}

welcome(); // 제대로 동작합니다.



// case 2

let age = prompt("나이를 알려주세요.", 18);

let welcome = (age < 18) ?
  function() { alert("안녕!"); } :
  function() { alert("안녕하세요!"); };

welcome(); // 제대로 동작합니다.
```

#### 요약
- 함수는 값입니다. 따라서 함수도 값처럼 할당, 복사, 선언할 수 있습니다.
- “함수 선언(문)” 방식으로 함수를 생성하면, 함수가 독립된 구문 형태로 존재하게 됩니다.
- “함수 표현식” 방식으로 함수를 생성하면, 함수가 표현식의 일부로 존재하게 됩니다.
- 함수 선언문은 코드 블록이 실행되기도 전에 처리됩니다. 따라서 블록 내 어디서든 활용 가능합니다.
- 함수 표현식은 실행 흐름이 표현식에 다다랐을 때 만들어집니다.

- 함수를 선언해야 한다면 함수가 선언되기 이전에도 함수를 활용할 수 있기 때문에, 함수 선언문 방식을 따르는 게 좋습니다. 함수 선언 방식은 코드를 유연하게 구성할 수 있도록 해주고, 가독성도 좋습니다.

- 함수 표현식은 함수 선언문을 사용하는게 부적절할 때에 사용하는 것이 좋습니다. 이번 챕터에서 함수 선언문을 사용해야만 하는 경우를 몇 가지 알아보았는데, 튜토리얼 뒤쪽에서 좀 더 깊게 해당 사례를 살펴보도록 하겠습니다.

---

### 화살표 함수 기본 
- 함수 표현식보다 단순하고 간결한 문법으로 함수를 만들 수 있는 방법 ⇒ _화살표 함수(arrow function)_

```js
let func = (arg1, arg2, ...argN) => expression
```

- 이렇게 코드를 작성하면 인자 `arg1..argN`를 받는 함수 `func`이 만들어집니다. 함수 `func`는 화살표(=>) 우측의 `표현식(expression)`을 평가하고, 평가 결과를 반환합니다.

```js
let func = function(arg1, arg2, ...argN) {
  return expression;
};
```
- 위 화살표 함수와 기능 동일

- 구체적인 예시
```js
// case 1
let sum = (a,b) => a + b; 

/* 위 화살표 함수는 아래 함수의 축약 버전입니다.

let sum = function(a, b) {
  return a + b;
};
*/

alert( sum(1, 2) ); // 3

// case 2 
// 인수가 하나라면 괄호 생략 가능!
let double = n => n * 2;

alert(double(3)); // 6


// case 3
// 인수가 하나도 없을 땐 괄호를 비워놓으면 됩니다. 다만, 이 때 괄호는 생략할 수 없습니다.
let sayHi = () => alert("안녕하세요!");

sayHi();

// case 4
// 함수 표현식과 같이 동적으로 사용 가능
let age = prompt("나이를 알려주세요.", 18);

let welcome = (age < 18) ?
  () => alert('안녕') :
  () => alert("안녕하세요!");

welcome();
```

#### 본문이 여러 줄인 화살표 함수
```js
let sum = (a, b) => {  // 중괄호는 본문 여러 줄로 구성되어 있음을 알려줍니다.
  let result = a + b;
  return result; // 중괄호를 사용했다면, return 지시자로 결괏값을 반환해주어야 합니다.
};

alert( sum(1, 2) ); // 3
```
- 👉 중괄호와 세미콜론, return 지시자를 명시해 줘야 한다. 


#### 요약
- 화살표 함수는 본문이 한 줄인 함수를 작성할 때 유용합니다. 본문이 한 줄이 아니라면 다른 방법으로 화살표 함수를 작성해야 합니다.

1. 중괄호 없이 작성: (...args) => expression – 화살표 오른쪽에 표현식을 둡니다. 함수는 이 표현식을 평가하고, 평가 결과를 반환합니다.
2. 중괄호와 함께 작성: (...args) => { body } – 본문이 여러 줄로 구성되었다면 중괄호를 사용해야 합니다. 다만, 이 경우는 반드시 return 지시자를 사용해 반환 값을 명기해 주어야 합니다.