---
tags : [ModernJavaScript, JS]
---
## JS 기본2
```ad-note
- [[#if와 '?'를 사용한 조건 처리|if와 '?'를 사용한 조건 처리]]
- [[#논리연산자|논리연산자]]
- [[#nullish 병합 연산자 '??'|nullish 병합 연산자 '??']]
- [[#while 과 for 반복문|while 과 for 반복문]]
- [[#Switch문|Switch문]]
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



### if와 '?'를 사용한 조건 처리
#### if 문
```js
let year = prompt('ECMAScript-2015 명세는 몇 년도에 출판되었을까요?', '');

if (year == 2015) alert( '정답입니다!' );
```

```js
if (year == 2015) {
  alert( "정답입니다!" );
  alert( "아주 똑똑하시네요!" );
}
```
- 👉 if문을 쓸 때는 조건이 참일 경우 실행되는 구문이 단 한 줄이더라도 중괄호 {}를 사용해 코드를 블록으로 감싸는 것을 추천해 드립니다. 이렇게 하면 코드 ***가독성이 증가***합니다.

#### 불린형으로의 변환
```js
// 아래 예시의 코드 블록은 절대 실행되지 않습니다.
if (0) { // 0은 falsy입니다. 
	... 
}

// 아래 예시의 코드 블록은 항상 실행됩니다.
if (1) { // 1은 truthy입니다.
  ...
}

// 아래와 같이 평가를 통해 확정된 불린값을 `if`문에 전달할 수도 있습니다.
let cond = (year == 2015); // 동등 비교를 통해 true/false 여부를 결정합니다. 
if (cond) { 
	... 
	}
  
```

#### else & else if
```js
let year = prompt('ECMAScript-2015 명세는 몇 년도에 출판되었을까요?', '');

if (year == 2015) {
  alert( '정답입니다!' );
} else {
  alert( '오답입니다!' ); // 2015 이외의 값을 입력한 경우
}


/////////////////////////////////////////////////////////////

let year = prompt('ECMAScript-2015 명세는 몇 년도에 출판되었을까요?', '');

if (year < 2015) {
  alert( '숫자를 좀 더 올려보세요.' );
} else if (year > 2015) {
  alert( '숫자를 좀 더 내려보세요.' );
} else {
  alert( '정답입니다!' );
}
```

#### 조건부 연산자 ‘?’
- 조건에 따라 다른 값을 변수에 할당해줘야 할 때가 있습니다.

```js
let accessAllowed;
let age = prompt('나이를 입력해 주세요.', '');

if (age > 18) {
  accessAllowed = true;
} else {
  accessAllowed = false;
}

alert(accessAllowed);
```

- '물음표(question mark) 연산자’라고도 불리는 '조건부(conditional) 연산자’를 사용하면 위 예시를 더 짧고 간결하게 변형할 수 있습니다.

- 조건부 연산자는 물음표?로 표시합니다. 피연산자가 세 개이기 때문에 조건부 연산자를 '삼항(ternary) 연산자’라고 부르는 사람도 있습니다. 참고로, 자바스크립트에서 피연산자를 3개나 받는 연산자는 조건부 연산자가 유일합니다.

```js
let result = condition ? value1 : value2;

let accessAllowed = (age > 18) ? true : false;
// 괄호가 있으나 없으나 차이는 없지만, 코드의 가독성 향상을 위해 괄호를 사용할 것을 권유합니다.
```
- 👉 평가 대상인 condition이 truthy라면 value1이, 그렇지 않으면 value2가 반환됩니다.


#### 다중 ‘?’
- 물음표 연산자?를 여러 개 연결하면 복수의 조건을 처리할 수 있습니다.
```js
let age = prompt('나이를 입력해주세요.', 18);

let message = (age < 3) ? '아기야 안녕?' :
  (age < 18) ? '안녕!' :
  (age < 100) ? '환영합니다!' :
  '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';

alert( message );
```

```ad-tip
- 위 예시와 동일하게 작동하는 구문
	```js
	if (age < 3) {
	  message = '아기야 안녕?';
	} else if (age < 18) {
	  message = '안녕!';
	} else if (age < 100) {
	  message = '환영합니다!';
	} else {
	  message = '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';
	}
	```
```


### 논리연산자
#### || (OR)
```js
alert( true || true );   // true
alert( false || true );  // true
alert( true || false );  // true
alert( false || false ); // false

let hour = 12;
let isWeekend = true;

if (hour < 10 || hour > 18 || isWeekend) {
  alert( '영업시간이 아닙니다.' ); // 주말이기 때문임
}
```

#### 첫 번째 truthy를 찾는 OR 연산자 ‘||’
- 이때, OR ||연산자는 다음 순서에 따라 연산을 수행합니다.
	1. 가장 왼쪽 피연산자부터 시작해 오른쪽으로 나아가며 피연산자를 평가합니다.
	2. 각 피연산자를 불린형으로 변환합니다. 변환 후 그 값이 true이면 연산을 멈추고 해당 피연산자의 변환 전 원래 값을 반환합니다.
	3. 피연산자 모두를 평가한 경우(모든 피연산자가 false로 평가되는 경우)엔 마지막 피연산자를 반환합니다.

```js
alert( 1 || 0 ); // 1 (1은 truthy임)

alert( null || 1 ); // 1 (1은 truthy임)
alert( null || 0 || 1 ); // 1 (1은 truthy임)

alert( undefined || null || 0 ); // 0 (모두 falsy이므로, 마지막 값을 반환함)
```

##### 변수 또는 표현식으로 구성된 목록에서 첫 번째 truthy 얻기
```js
let firstName = "";
let lastName = "";
let nickName = "바이올렛";

alert( firstName || lastName || nickName || "익명"); // 바이올렛
```

##### 단락 평가
```js
// 아래 예시를 실행하면 두 번째 메시지만 출력됩니다.

true || alert("not printed");
false || alert("printed");
```
- 👉 첫 번째 줄의 `||` 연산자는 `true`를 만나자마자 평가를 멈추기 때문에 `alert`가 실행되지 않습니다.

#### && (AND)
```js
alert( true && true );   // true
alert( false && true );  // false
alert( true && false );  // false
alert( false && false ); // false

let hour = 12;
let minute = 30;

if (hour == 12 && minute == 30) {
  alert( '현재 시각은 12시 30분입니다.' );
}
```


#### 첫 번째 falsy를 찾는 AND 연산자 ‘&&’
```js
// 첫 번째 피연산자가 truthy이면,
// AND는 두 번째 피연산자를 반환합니다.
alert( 1 && 0 ); // 0
alert( 1 && 5 ); // 5

// 첫 번째 피연산자가 falsy이면,
// AND는 첫 번째 피연산자를 반환하고, 두 번째 피연산자는 무시합니다.
alert( null && 5 ); // null
alert( 0 && "아무거나 와도 상관없습니다." ); // 0
```

```js
alert( 1 && 2 && null && 3 ); // null
alert( 1 && 2 && 3 ); // 마지막 값, 3
```

#### ! (NOT)
```js
alert( !true ); // false
alert( !0 ); // true
```

```js
alert( !!"non-empty string" ); // true
alert( !!null ); // false
```
- 👉==NOT을 두 개 연달아 사용(!!)하면 값을 불린형으로 변환할 수 있습니다.==
	- 이때, 첫 번째 NOT 연산자는 피연산자로 받은 값을 불린형으로 변환한 후 이 값의 역을 반환하고, 두 번째 NOT 연산자는 첫 번째 NOT 연산자가 반환한 값의 역을 반환합니다. 이렇게 NOT을 연달아 사용하면 특정 값을 불린형으로 변환할 수 있습니다.

### nullish 병합 연산자 '??'
- nullish 병합 연산자(nullish coalescing operator) ??를 사용하면 짧은 문법으로 여러 피연산자 중 그 값이 ‘확정되어있는’ 변수를 찾을 수 있습니다.

- a ?? b의 평가 결과는 다음과 같습니다.
	- a가 null도 아니고 undefined도 아니면 a
	- 그 외의 경우는 b

```js
let firstName = null;
let lastName = null;
let nickName = "바이올렛";

// null이나 undefined가 아닌 첫 번째 피연산자
alert(firstName ?? lastName ?? nickName ?? "익명의 사용자"); // 바이올렛
```

```ad-tip
- ?? 와 ||의 차이
	- ||는 첫 번째 truthy 값을 반환합니다.
	- ??는 첫 번째 정의된(defined) 값을 반환합니다.
	```js
	let height = 0;
	
	alert(height || 100); // 100
	alert(height ?? 100); // 0
	```
```

- ??의 연산자 우선순위는 대다수의 연산자보다 낮고 ?와 = 보다는 높습니다.
- 괄호 없이 ??를 ||나 &&와 함께 사용하는 것은 금지되어있습니다.

### while 과 for 반복문
```js
while (condition) {
  // 코드
  // '반복문 본문(body)'이라 불림
}

//////////////////////////////////////////////////////
let i = 0;
while (i < 3) { // 0, 1, 2가 출력됩니다.
  alert( i );
  i++;
}


//////////////////////////////////////////////////////
let i = 3;
while (i) { // i가 0이 되면 조건이 falsy가 되므로 반복문이 멈춥니다.
  alert( i );
  i--;
}
```

```ad-tip
- 본문이 한 줄이면 대괄호를 쓰지 않아도 됩니다.
	```js
	let i = 3;
	while (i) alert(i--);
	```
```

#### do ... while 반복
```js
do {
  // 반복문 본문
} while (condition);

let i = 0;
do {
  alert( i );
  i++;
} while (i < 3);
```
- 👉 do..while 문법은 조건이 truthy 인지 아닌지에 상관없이, ***본문을 최소한 한 번이라도 실행하고 싶을 때만 사용***해야 합니다. 

#### for 반복문
```js
for (begin; condition; step) {
  // ... 반복문 본문 ...
}

for (let i = 0; i < 3; i++) { // 0, 1, 2가 출력됩니다.
  alert(i);
}
```

| begin     | i = 0    | 반복문에 진입할 때 단 한 번 실행됩니다.               |
|-----------|----------|---------------------------------------|
| condition | i < 3    | 반복마다 해당 조건이 확인됩니다. false이면 반복문을 멈춥니다. |
| body      | alert(i) | condition이 truthy일 동안 계속해서 실행됩니다.     |
| step      | i++      | 각 반복의 body가 실행된 이후에 실행됩니다.            |

#### 반복문 빠져나오기
- `break`를 사용하면 언제든 원하는 때에 반복문을 빠져나올 수 있습니다.
```js
let sum = 0;

while (true) {

  let value = +prompt("숫자를 입력하세요.", '');

  if (!value) break; // (*)

  sum += value;

}
alert( '합계: ' + sum );
```

- `continue`는 현재 반복을 종료시키고 다음 반복으로 넘어가고 싶을 때 사용할 수 있습니다.
```js
for (let i = 0; i < 10; i++) {

  // 조건이 참이라면 남아있는 본문은 실행되지 않습니다.
  if (i % 2 == 0) continue;

  alert(i); // 1, 3, 5, 7, 9가 차례대로 출력됨
}
```

#### break/continue와 레이블
- 여러 개의 중첩 반복문을 한 번에 빠져나와야 하는 경우가 종종 생기곤 합니다.

- 반복문 안에서 `break <labelName>`문을 사용하면 레이블에 해당하는 반복문을 빠져나올 수 있습니다.

```js
labelName: for (...) {
  ...
}


outer: for (let i = 0; i < 3; i++) {

  for (let j = 0; j < 3; j++) {

    let input = prompt(`(${i},${j})의 값`, '');

    // 사용자가 아무것도 입력하지 않거나 Cancel 버튼을 누르면 두 반복문 모두를 빠져나옵니다.
    if (!input) break outer; // (*)

    // 입력받은 값을 가지고 무언가를 함
  }
}
alert('완료!');
```


```ad-caution
- 레이블은 마음대로 '점프’할 수 있게 해주지 않습니다.
	- 레이블을 사용한다고 해서 원하는 곳으로 마음대로 점프할 수 있는 것은 아닙니다.
	- 아래 예시처럼 레이블을 사용하는 것은 불가능합니다.
	```js
	break label; // 아래 for 문으로 점프할 수 없습니다.

	label: for (...)
	```
- `break`와 `continue`는 반복문 안에서만 사용할 수 있고, 레이블은 반드시 `break`이나 `continue` 지시자 위에 있어야 합니다.
```

##### 요약
- 지금까지 세 종류의 반복문에 대해 살펴보았습니다.
	- while – 각 반복이 시작하기 전에 조건을 확인합니다.
	- do..while – 각 반복이 끝난 후에 조건을 확인합니다.
	- for (;;) – 각 반복이 시작하기 전에 조건을 확인합니다. 추가 세팅을 할 수 있습니다.
- ‘무한’ 반복문은 보통 while(true)를 써서 만듭니다. 무한 반복문은 여타 반복문과 마찬가지로 break 지시자를 사용해 멈출 수 있습니다.
- 현재 실행 중인 반복에서 더는 무언가를 하지 않고 다음 반복으로 넘어가고 싶다면 continue 지시자를 사용할 수 있습니다.
- 반복문 앞에 레이블을 붙이고, break/continue에 이 레이블을 함께 사용할 수 있습니다. 레이블은 중첩 반복문을 빠져나와 바깥의 반복문으로 갈 수 있게 해주는 유일한 방법입니다.


### Switch문
- 복수의 `if` 조건문은 `switch`문으로 바꿀 수 있습니다.
- `switch`문은 하나 이상의 `case`문으로 구성됩니다. 대개 `default`문도 있지만, 이는 필수는 아닙니다.

```js
switch(x) {
  case 'value1':  // if (x === 'value1')
    ...
    [break]

  case 'value2':  // if (x === 'value2')
    ...
    [break]

  default:
    ...
    [break]
}
```

```ad-tip
- `switch/case`문의 인수엔 어떤 표현식이든 올 수 있습니다.
- `switch`문과 `case`문은 모든 형태의 표현식을 인수로 받습니다.
	```js
	let a = "1";
	let b = 0;
	
	switch (+a) {
	  case b + 1:
	    alert("표현식 +a는 1, 표현식 b+1는 1이므로 이 코드가 실행됩니다.");
	    break;
	
	  default:
	    alert("이 코드는 실행되지 않습니다.");
	}
	```
```


#### 여러 개의 case 문 묶기
```js
let a = 3;

switch (a) {
  case 4:
    alert('계산이 맞습니다!');
    break;

  case 3: // (*) 두 case문을 묶음
  case 5:
    alert('계산이 틀립니다!');
    alert("수학 수업을 다시 들어보는걸 권유 드립니다.");
    break;

  default:
    alert('계산 결과가 이상하네요.');
}
```
- 👉 3, 5 case일 경우 동일한 결과를 출력함

#### 자료형의 중요성
```js
let arg = prompt("값을 입력해주세요.");
switch (arg) {
  case '0':
  case '1':
    alert( '0이나 1을 입력하셨습니다.' );
    break;

  case '2':
    alert( '2를 입력하셨습니다.' );
    break;

  case 3:
    alert( '이 코드는 절대 실행되지 않습니다!' );
    break;
  default:
    alert( '알 수 없는 값을 입력하셨습니다.' );
}
```