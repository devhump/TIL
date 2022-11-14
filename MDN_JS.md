#### 스크립트 로딩 전략

```javascript
<script async src="js/vendor/jquery.js"></script>
<script async src="js/script2.js"></script>
<script async src="js/script3.js"></script>

<script defer src="js/vendor/jquery.js"></script>
<script defer src="js/script2.js"></script>
<script defer src="js/script3.js"></script>
```

- `async`와 `defer` 모두, 브라우저가 페이지의 다른 내용(DOM 등등)을 불러오는 동안 스크립트를 별도 스레드에서 불러오게 만듭니다. 덕분에 스크립트를 가져오는 동안 페이지 로딩이 중단되지 않습니다.
- `async` 특성을 지정한 스크립트는 다운로드가 끝나는 즉시 실행합니다. 실행은 현재 페이지 렌더링을 중단하며, 실행 순서는 보장되지 않습니다.
- `defer` 특성을 지정한 스크립트는 순서를 유지한 채로 가져오며 모든 콘텐츠를 다 불러온 이후에 실행합니다.
- 의존성 없는 스크립트를 불러온 즉시 실행하려면 `async`를 사용하세요.
- 다른 스크립트에 의존하거나 DOM 로딩이 필요한 스크립트에는 `defer`를 사용하고, 원하는 순서에 맞춰서 `<script>` 요소를 배치하세요.
- 



#### 주석처리

```javascript
// 한줄 주석 처리

/*
 여러줄
 주석 처리
*/
```

- [JavaScript가 뭔가요?](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript)





### 비교 연산자

| 연산자 | 이름                       |
| ------ | -------------------------- |
| `===`  | 엄격 일치 (정확히 같은가?) |
| `!==`  | 불일치 (같지 않은가?)      |
| `<`    | 미만                       |
| `>`    | 초과                       |



```javascript
5 === 2 + 4 // false
'Chris' === 'Bob' // false
5 === 2 + 3 // true
2 === '2' // false, 숫자와 문자열은 다름


5 !== 2 + 4 // true
'Chris' !== 'Bob' // true
5 !== 2 + 3 // false
2 !== '2' // true, 숫자와 문자열은 다름


6 < 10 // true
20 < 10 // false


6 > 10 // false
20 > 10  // true
```



- `for ~ of` : 반복가능한 객체(Array, Map, Set, String, TypedArray, arguments 객체 등) 에 대해서 반복하고 각 개별 속성 값에 대해 실행되는 문이 있는 사용자 정의 반복 후크를 호출하는 루프를 생성합니다. 

  ```javascript
  for (variable of iterable) {
      statement
  }
  
  // variable: 각 반복에 서로 다른 속성값이 variable에 할당됩니다.
  // iterable: 반복되는 열거가능(enumerable)한 속성이 있는 객체.
  ```

  

  ```javascript
  //예시 코드 
  
  const array1 = ['a','b','c'];
  
  for (const element of array1){
      console.log(element);
  }
  
  // "a"
  // "b"
  // "c"
  ```



- `for ~ of` 와 `for ~ in`의 차이 

  `for ~ in` 루프는 객체의 열거 가능한 속성에 대해 반복합니다. `for...of` 구문은 **컬렉션** 전용입니다. 모든 객체보다는, `[Symbol.iterator]` 속성이 있는 모든 컬렉션 요소에 대해 이 방식으로 반복합니다.



```javascript
Object.prototype.objCustom = function () {};
Array.prototype.arrCustom = function () {};

let iterable = [3, 5, 7];
iterable.foo = "hello";

for (let i in iterable) {
  console.log(i); // logs 0, 1, 2, "foo", "arrCustom", "objCustom"
}

for (let i of iterable) {
  console.log(i); // logs 3, 5, 7
}

```



- `for ~ in` 문은 상속된 열거 가능한 속성들을 포함하여 객체에서 문자열로 키가 지정된 모든 열거 가능한 속성에 대해 반복합니다. 

- 임의의 순서로 객체의 속성들에 대해 반복 -> 인덱스의 순서가 중요한 [`Array`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array)에서 반복을 위해 사용할 수 없음

  ```javascript
  for (const variable in object) {
    statement
  }
  
  // variable :매번 반복마다 다른 속성이름(Value name)이 변수(variable)로 지정됩니다.
  // object :반복작업을 수행할 객체로 열거형 속성을 가지고 있는 객체.
  ```

  

  ```javascript
  // 예시 코드
  
  const object = { a:1, b:2, c:3 };
  
  for (const propety in object){
  	console.log(`${property}: ${object[property]}`);
  }
  
  > "a: 1"
  > "b: 2"
  > "c: 3"
  ```

  



### 배열 in JS

- JavaScript에서 배열이란 일반적으로 "리스트같은 객체(list-like objects)"를 말한다. 
- 배열은 보통 리스트에 저장된 다수의 값들을 포함하고 있는 하나의 객체.
- 배열의 요소가 될 수 있는 것 : 문자열, 숫자, 개체, 다른 변수, 심지어 다른 배열

```javascript
var shopping = ['bread', 'milk', 'cheese', 'hummus', 'noodles'];
shopping;


// 인덱스를 활용한 요소 확인
shopping[0];
// returns "bread"

// 요소의 변경
shopping[0] = 'tahini';

var sequence = [1, 1, 2, 3, 5, 8, 13];
var random = ['tree', 795, [0, 1, 2]];
```



- 배열의 개수

  ```javascript
  sequence.length;
  // should return 7
  
  // 반복문을 활용한 요소 출력
  var sequence = [1, 1, 2, 3, 5, 8, 13];
  for (var i = 0; i < sequence.length; i++) {
    console.log(sequence[i]);
  }
  
  
  ```

  

- 배열의 메서드 (문자열 ◀▶ 배열 변환)

  - `split()`

    ```javascript
    var myData = 'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle';
    
    var myArray = myData.split(',');
    myArray;
    //(6) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle']
    ```

    ```javascript
    myArray.length;
    myArray[0]; // the first item in the array
    myArray[1]; // the second item in the array
    myArray[myArray.length-1]; // the last item in the array
    ```

  - `join()`

    ```javascript
    var myNewString = myArray.join(','); // , 말고 다른 구분자 사용가능
    myNewString;
    //'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle'
    
    ```

  - `toString()`

    ```javascript
    var dogNames = ['Rocket','Flash','Bella','Slugger'];
    dogNames.toString(); //Rocket,Flash,Bella,Slugger
    ```

    `join()` 을 사용하면 다른 구분자를 지정할 수 있지만, `toString()` 은 항상 콤마를 사용합니다.

    

- 배열에 원소를 추가 / 제거

  - `push()` 

    ```javascript
    myArray.push('Cardiff');
    myArray;
    //(7) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff']
    
    myArray.push('Bradford', 'Brighton');
    myArray;
    //(9) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff', 'Bradford', 'Brighton']
    
    var newLength = myArray.push('Bristol'); //새로운 배열의 길이 return 
    myArray;
    newLength;
    ```

  - `pop()` 

    ```javascript
    myArray.pop();
    // 'Bristol'
    
    var removedItem = myArray.pop();
    myArray;
    removedItem;
    ```

  - `unshift()` & `shift()`

    ```javascript
    // myArray = (8) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff', 'Bradford']
    
    myArray.unshift('Edinburgh');
    myArray;
    //(9) ['Edinburgh', 'Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff', 'Bradford']
    
    var removedItem = myArray.shift();
    myArray;
    removedItem;
    //'Edinburgh'
    ```

    



---

### 함수

```javascript
// 함수의 정의와 호출
function myFunction() {
  alert('hello');
}

myFunction()
// calls the function once
```



- 익명함수 : 주로 이벤트 핸들러와 사용됨

  ```javascript
  // 함수 이름을 설정하지 않음
  function() {
    alert('hello');
  }
  
  
  var myButton = document.querySelector('button');
  
  myButton.onclick = function() {
    alert('hello');
  }
  ```



- *함수 표현식*(function expression)  ▶ 변수 속에 익명 함수 넣기

  - 함수 선언과는 다르게, 함수 표현식은 호이스팅되지 않음

  ```javascript
  var myGreeting = function() {
    alert('hello');
  }
  
  myGreeting();
  
  // 다중 변수들에 함수 할당하기 : 권장하지 않음
  var anotherGreeting = function() {
    alert('hello');
  }
  
  myGreeting();
  anotherGreeting();
  ```

  

- 함수 스코프와 충돌(conflicts)

  ```html
  <!-- Excerpt from my HTML -->
  <script src="first.js"></script>
  <script src="second.js"></script>
  <script>
    greeting();
  </script>
  ```

  ```javascript
  // first.js
  var name = 'Chris';
  function greeting() {
    alert('Hello ' + name + ': welcome to our company.');
  }
  
  // second.js
  var name = 'Zaptec';
  function greeting() {
    alert('Our company is called ' + name + '.');
  }
  ```

  - 둘다 `greeting()` 이라는 이름의 함수를 가지고 있음

    ▶ **But 첫번째 함수(`first.js`)에만 접근 가능**

  - 또, `second.js` 파일에서 `let` 키워드로 `name` 변수를 두 번째로 선언하려고 시도하는 것은 오류 발생



---



### 문자열

```javascript
var string = 'The revolution will not be televised.';
string;

var badString = string;
badString;
// 'The revolution will not be televised.'

```

- 문자열의 시작과 끝에는 `'` 또는  `"` 사용 -> 하나가 빠지면 에러 발생
- 문자열 내부에 `'` 또는 `"` 사용 -> `'따옴표 내부 "쌍따옴표 사용" '`
- 또는 이스케이스 문자 사용 `\` 



- 문자열 결합

  ```javascript
  var one = 'Hello, ';
  var two = 'how are you?';
  var joined = one + two;
  joined;
  
  var multiple = one + one + one + one + two;
  multiple;
  
  var response = one + 'I am fine — ' + two;
  response;
  ```

  

- 문자열 - 숫자

  ```javascript
  // 숫자형으로 변환 
  var myString = '123';
  var myNum = Number(myString);
  typeof myNum;
  
  // 문자형으로 변환
  var myNum = 123;
  var myString = myNum.toString();
  typeof myString;
  
  ```

- 문자열 조작

  ```javascript
  var browserType = 'mozilla';
  browserType.length;
  
  // 인덱스를 활용한 문자열 접근
  browserType[0];
  browserType[browserType.length - 1];
  
  // 전체 문자열이 해당 문자열을 포함 하고 있는지 확인 할 때
  browserType.indexOf('zilla');
  // 2
  browserType.indexOf('vanilla');
  // -1  // 해당 문자열을 포함하지 않을 때
  
  // 슬라이싱을 통한 문자열 추출
  browserType.slice(0, 3);
  // moz
  browserType.slice(2);
  // zilla
  
  // 대소문자 변경
  var radData = 'My NaMe Is MuD';
  radData.toLowerCase();
  radData.toUpperCase();
  
  // 문자열 대체
  browserType.replace('moz', 'van');
  // 'vanilla'
  
  // 문자열 포함하고 있는지 확인
  if (greeting.includes('Christmas')) {
  	//
  }
  
  ```

  

### 변수

- 변수 선언에 대한 규칙
  - `0-9`, `a-z`, `A-Z`, underbar(`_`) 사용
  - 변수에 이름 시작에 `_` 또는 숫자 사용 X
  - CamelCase 사용, 대소문자 구분
