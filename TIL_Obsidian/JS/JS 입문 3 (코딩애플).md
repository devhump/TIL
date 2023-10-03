---
tag: [CodingApple/JS, JS]
---

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

### Array 와 Object 자료형
#### Array 자료형
- 여러가지 자료를 한곳에 저장하고 싶을 때 사용하는 자료형입니다.
- 저장된 데이터의 **순서가 있음** → 인덱싱 가능
```js
var car = ['소나타', 50000, 'white'];

// 인덱싱을 통한 항목 선택 가능
console.log(car[1]);

// 특정 인덱스의 값 수정 가능 
car[1] = 60000;

console.log(car.slice(1,2)); // [50000] 출력
```

#### Object 자료형 
- 여러가지 자료를 한곳에 저장하고 싶을 때 사용하는 자료형입니다.
- `key : value` 형태로 데이터 저장
- - 저장된 데이터의 **순서가 없음**
```js
var car2 = { name : '소나타', price : 50000 };

console.log(car2['name']);
console.log(car2.name);
```

- 데이터 접근 방법
```js
var car2 = { name : '소나타', price : 50000 };

car2['key값']
car2.key값

// key를 활용해 데이터 수정 가능
car2['name'] = '그랜저';
car2.price = 60000;
```


#### Array/Object 차이
- 순서개념의 유무 → `Array` 로 가능한 것
	- 가나다순 정렬
	- x번 자료부터 y번 자료까지 자르기
	- x번 자료 바꾸기
	- 맨 뒤, 맨 앞에 자료 넣기
	- 원하는 자료가 들어있나 검색

- Array의 기본 함수
```js
array자료.sort() // 가나다순 정렬되고
array자료.slice(x, y) // x번부터 y번 전까지 자를 수 있고 
array자료.push(x) // x를 맨 뒤에 입력할 수 있고
```


```ad-todo
- **오늘의 숙제** 
	```html
	<div class="container mt-3">
	  <div class="card p-3">
	    <span>상품명</span>
	    <span>가격</span>
	  </div>
	</div> 
	
	<script>
	  var car2 = { name : '소나타', price : 50000 } 
	</script>
	```
- 여기서 car2 에 저장된 소나타라는 상품명과 50000이라는 가격을 뽑아서 html에 집어넣어보십시오.

- 자바스크립트 작성해서 구현합시다. 
```

```html
  <div class="container mt-3">
    <div class="card p-3">
      <span id="productName">상품명</span>
      <span id="productPrice">가격</span>
    </div>
  </div>

  <script>
    var car2 = { name : '소나타', price : 50000 } 

    document.querySelector('#productName').innerHTML = car2['name'];
    $("#productPrice").text(`${car2['price']}`);

  </script>
```

### 약간 복잡한 Array & Object 데이터바인딩
#### 조금 더 복잡한 자료를 다뤄봅시다
```html
<div class="container mt-3">
  <div class="card p-3">
    <span class="car-title">상품명</span>
    <span>가격</span>
  </div>
</div> 

<script>
  var car2 = { name : '소나타', price : [50000, 3000, 4000] } 
  document.querySelector('.car-title').innerHTML = car2.name;
</script>
```
- 👉 object 안에 array/object 또는 array 안에 array/object 가 포함 될 수 있다. 

```ad-tip
- object 자료형 사용 방법의 특징
	```js
	var car2 = { name : '소나타', price : 50000 };
	 
	car2.name
	car2['name']
	```
	- 위와 같은 자료형에 접근하는 방법은 2가지인데, 이때 아래와 같은 방법으로 <br>사용시 **추후 변수를 활용한 코드**를 짤 수 있다.
```

#### 복잡한 데이터에서 자료꺼내려면
- 데이터의 형태가 복잡할 때는 우선 console창에 출력을 해보자

![](assets/JS%20입문%203.png)
- 👆 위와 같이 중괄호(`{}`) 로 시작하는 경우, 대부분 **object 자료형**이다.

![](assets/JS%20입문%203-1.png)
- 👆 위와 같이 중괄호(`[]`) 로 시작하는 경우, 대부분 **Array 자료형**이다.

- object/Array 자료형이 중첩된 형태일 때
	- `car2['key값'][인덱스]`
	- `car2.키값[인덱스]`
	- 와 같은 형태로 접근 할 수 있다.

```js
var car2 = { name : '소나타', price : [50000, 3000, 4000] };

car2['key값'][인덱스]
car2.키값[인덱스]

car2['price'][0];
car2.price[0]

```

#### 실제 웹서비스 개발할 땐 2개 방식이 있는데
- 그냥 누가 내 사이트로 접속하면 html 이쁘게 만들어서 보내주는걸 웹서비스라고 합니다. 
- 근데 html을 누가 완성하는지에 따라 개발방식의 차이가 있습니다. 

1. **server-side rendering**
	- 서버에서 html을 미리 완성해서 고객에게 보내줌 
![](assets/JS%20입문%203-3.png)[^자료출처: 코딩애플]

2. **client-side rendering**
	- 서버가 비어있는 html과 데이터만 보내줌 <br>👉 그리고 자바스크립트를 이용해서 고객 브라우저안에서 html을 완성
![](assets/JS%20입문%203-4.png)[^자료출처: 코딩애플]

```ad-todo
- 오늘의 숙제 :
	- list.html 만들고 하단 코드를 복사붙여넣기합니다.
	- 그럼 상품 3개를 진열할 수 있는 카드레이아웃이 나옵니다. (bootstrap 필요) 
	- products 변수안에 상품데이터도 준비되어있는데
	- 자바스크립트를 열심히 짜서 3개의 상품 제목, 가격을 html에 전부 꽂아넣어오십시오.

	```html
	<div class="card-group container">
	  <div class="card">
	    <img src="https://via.placeholder.com/600">
	    <div class="card-body">
	      <h5>Card title</h5>
	      <p>가격 : 70000</p>
	      <button class="btn btn-danger">주문하기</button>
	    </div>
	  </div>
	  <div class="card">
	    <img src="https://via.placeholder.com/600">
	    <div class="card-body">
	      <h5>Card title</h5>
	      <p>가격 : 70000</p>
	      <button class="btn btn-danger">주문하기</button>
	    </div>
	  </div>
	  <div class="card">
	    <img src="https://via.placeholder.com/600">
	    <div class="card-body">
	      <h5>Card title</h5>
	      <p>가격 : 70000</p>
	      <button class="btn btn-danger">주문하기</button>
	    </div>
	  </div>
	</div>
	
	<script>
	  var products = [
	    { id : 0, price : 70000, title : 'Blossom Dress' },
	    { id : 1, price : 50000, title : 'Springfield Shirt' },
	    { id : 2, price : 60000, title : 'Black Monastery' }
	  ];
	</script> 
	```
```

```html
    <div class="card">
      <img src="https://via.placeholder.com/600">
      <div class="card-body">
        <h5 class="productTitle">Card title</h5>
        <p>가격 : 70000</p>
        <button class="btn btn-danger">주문하기</button>
      </div>
    </div>
```

```js
var products = [
  { id : 0, price : 70000, title : 'Blossom Dress' },
  { id : 1, price : 50000, title : 'Springfield Shirt' },
  { id : 2, price : 60000, title : 'Black Monastery' }
]; 

for (let i = 0; i < 3; i++){
  dataUpdate(i);
}

function dataUpdate(idx) {
  document.querySelectorAll('.productTitle')[idx].innerHTML = products[idx]['title'];
  document.querySelectorAll('.card-body p')[idx].innerHTML = `가격 : ${products[idx].price}`;
}
```

### 데이터바인딩 숙제 & 문자중간에 변수넣는 법
#### 저번시간 숙제는
- 첫째 상품명을 뽑는 법을 알아봅시다.
```js
var products = [
  { id : 0, price : 70000, title : 'Blossom Dress' },
  { id : 1, price : 50000, title : 'Springfield Shirt' },
  { id : 2, price : 60000, title : 'Black Monastery' }
]; 
```

```js
products = [{}, {}, {}] 
```
- Array 안에 object가 있는 형태
	- 👉 `products[0]` → 인덱스로 접근!

```js
products[0] = { id : 0, price : 70000, title : 'Blossom Dress' }
```
- object 형태
	- 👉 `products[0].price` 또는 `products[0]['price']`로 접근!


```ad-tip
- 추가 클래스 삽입 없이 셀렉터로 접근하려면?
	```html
	<div class="card">
      <img src="https://via.placeholder.com/600">
      <div class="card-body">
        <h5 class="productTitle">Card title</h5>
        <p>가격 : 70000</p>
        <button class="btn btn-danger">주문하기</button>
      </div>
    </div>
	```
- 👉 기존 클래스와 하위 태그 활용!
	```js
	document.querySelector('.card-body h5')[0].innerHTML;
	```
- `querySelector('.card-body h5')` 
	- 👉 `card-body` 클래스를 가진 요소의 자식  중에서 `<h5>` 태그를 가진 요소
```


#### 문자 중간에 변수 쉽게넣기
1. `+` 기호 활용
```js
var a = '안녕';
console.log('문자' + a + '문자');  // '문자안녕문자'출력됨
```

2. 백틱(backtick, `` ` `` ) 문법 활용
```js
var a = '안녕';
console.log(`문자 ${a} 문자`);  // '문자안녕문자'출력됨
```
- 👉 문자 중간에 엔터키 칠 수 있음


### Select 인풋 다루기
#### select 들어간 폼을 만들어봅시다
- `<select>` 는 `<input>` 이랑 똑같은데<br>사용자가 고를 수 있는 선택지를 드랍다운 메뉴로 제공하는 `<input>` 입니다. 
- 선택지는 `<option>`으로 넣으면 됩니다. 

```html
<form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
    </select>
</form>
```
- `<select>` 태그도 선택시 input, change 이벤트가 발생합니다.
- `<select>` 태그도 `.value`로 유저가 입력한 값을 가져올 수 있습니다.

#### 셔츠고르면 밑에 `<select>` 더 보여주기
- UI 어떻게 만든다고 했습니까
	- 👉 html css로 미리 디자인해놓고 원할 때 보여주기만 하면 됩니다

```html
<form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
    </select>
    <select class="form-select mt-2 form-hide">
      <option>95</option>
      <option>100</option>
    </select>
</form>
```

```css
.form-hide{
	display : none;
}
```
- `display : none` 을 포함하는 클래스 만들어서 탈부착하기
	- "유저가 셔츠선택하면 form-hide 제거해주세요~" 구현

```html
<script>
  if (유저가 선택한거 == '셔츠') {
    $('.form-select').eq(1).removeClass('form-hide');
  }
</script>
```

#### `<script>` 안에 대충 적은 코드는 페이지 로드시 1회 실행됨
```html
<script>
  var value = $('.form-select').eq(0).val();
  if (value == '셔츠') {
    $('.form-select').eq(1).removeClass('form-hide');
  }
</script>
```
- 👉 작동되지 않는이유?
	- ==페이지 로드시 1회 실행되고 다시는 실행되지 않기 때문==

```html
<script>
  $('.form-select').eq(0).on('input', function(){

    var value = $('.form-select').eq(0).val();
    if (value == '셔츠') {
      $('.form-select').eq(1).removeClass('form-hide');
    }

  });
</script>
```

```ad-tip
- **이벤트: change**
	- `change` 이벤트는 요소 변경이 끝나면 발생합니다.
	- 텍스트 입력 요소인 경우에는 요소 변경이 끝날 때가 아니라 포커스를 잃을 때 이벤트가 발생합니다.
- **이벤트: input**
	- input 이벤트는 사용자가 값을 수정할 때마다 발생합니다.
	- 키보드 이벤트와 달리 input 이벤트는 어떤 방법으로든 값을 변경할 때 발생합니다. 마우스를 사용하여 글자를 붙여 넣거나 음성인식 기능을 사용해 글자를 입력할 때처럼 키보드가 아닌 다른 수단을 사용하여 값을 변경시킬 때도 input 이벤트가 발생합니다.
- 참고: [이벤트: change, input, cut, copy, paste](https://ko.javascript.info/events-change-input)
```



```ad-todo
(응용)

1. 심심하면 '모자'를 선택했을 때 `<select>`를 다시 숨기는 기능도 만들어봅시다. 

2. 지금 비슷한 셀렉터들이 많은데 변수화하면 성능개선이 되겠군요

3. 이벤트리스너 안에서 e.currentTarget 아니면 this 이런거 써도 될듯요 
```

```html
  <form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
    </select>
    <select class="form-select mt-2 selectHidden" id="secondSelect">
      <option>90</option>
      <option>95</option>
      <option>100</option>
    </select>
  </form>
```

```js
 // 셀렉터 변수화
	let formSelect = $('.form-select').eq(0);
    let secondSelect = $("#secondSelect");
    
    formSelect.on('input', function(){
      let value = formSelect.val();
      if (value == '셔츠'){
        secondSelect.removeClass('selectHidden');
      } else {
        secondSelect.addClass('selectHidden');
      }
    });
```

```js
    let formSelect = $('.form-select').eq(0);
    let secondSelect = $("#secondSelect");
    
    formSelect.on('input', function(e){
      let value = e.currentTarget.value;
      // let value = this.value; 도 동일
      if (value == '셔츠'){
        secondSelect.removeClass('selectHidden');
      } else {
        secondSelect.addClass('selectHidden');
      }
    });
```
- `e.currentTarget`을 쓸 경우, `e.currentTarget.value`로 사용
- `let value = this.value;`도 동일하게 작동

### Select 2 : 자바스크립트로 html 생성하는 법
1. document.createElement()
```html
<div id="test">
  
</div>

<script>
    let a = document.createElement('p');
    a.innerHTML = '안녕';
//    a.classList.add();
    document.querySelector('#test').appendChild(a);
</script>
```

2. .insertAdjacentHTML()
```html
<div id="test">
  
</div>

<script>
// vanilla JS
var template = '<p>안녕</p>';
document.querySelector('#test').insertAdjacentHTML('beforeend', template); // 안쪽 맨 밑에 추가하라

// jQuery
$('#test').append(template);
</script>
```
- 👉 속도에서는 `createElement()`가 더 빨리 동작하나, 실질적으로는 크게 의미 없음

```ad-todo
(응용)

- 바지 눌렀다가 다시 셔츠 누르면 뭔가 이상해지는 문제도 해결해보면 어떨까요.
	- 셔츠눌렀을 때 둘 째 `<select>` 안에 있는 html도 조정해줘야겠군요.
```

```html
  <form class="container my-5 form-group">
    <p>상품선택</p>
    <select class="form-select mt-2">
      <option>모자</option>
      <option>셔츠</option>
      <option>바지</option>
    </select>
    <select class="form-select mt-2 selectHidden" id="secondSelect">
    </select>
  </form>
```

```js
    // select 인풋 
    let formSelect = $('.form-select').eq(0);
    let secondSelect = $("#secondSelect");

    formSelect.on('input', function() {
      let value = this.value;
      if (value == '셔츠') {

        let shirtsSize = [90, 95, 100]

        secondSelect.html("");
        for (let i = 0; i < shirtsSize.length; i++) {
          document.querySelector('#secondSelect').insertAdjacentHTML('beforeend', `<option>${shirtsSize[i]}</option>`);
        }
        secondSelect.removeClass('selectHidden');
      } else if (value == '바지') {

        let pantsSize = [28, 29, 30]

        secondSelect.html("");
        for (let i = 0; i < pantsSize.length; i++) {
          document.querySelector('#secondSelect').insertAdjacentHTML('beforeend', `<option>${pantsSize[i]}</option>`);
        }
        secondSelect.removeClass('selectHidden');
      } else {
        secondSelect.addClass('selectHidden');
      }
    });
```
- 👉 옷 종류별 사이즈 저장 → 해당 옵션 선택시 마다 종류별 사이즈 출력

### Select 3 : forEach, for in 반복문
#### forEach() 반복문
- array 자료 뒤에 붙일 수 있는 **forEach()** 라는 기본함수가 있습니다.
```js
var pants = [28, 30, 32];
pants.forEach(function(){
  console.log('안녕') // '안녕'이 세번 출력됨
});
```

- 콜백함수 안에 파라미터 2개까지 작명이 가능
```js
var pants = [28, 30, 32];

pantsSize.forEach(function(a, i){
  secondSelect.append(`<option>${a}</option>`)
}
```
- 👉 이때, 첫 파라미터(`a`)는 **반복문 돌 때 마다 array 안에 있던 하나하나의 데이터**가 되고,<br>둘 째 파라미터(`i`)는 반복문 돌 때 마다 0부터 1씩 증가하는 정수가 됩니다.

- forEach()를 활용한 코드 
```js
// forEach 반복문의 사용

    // select 인풋 
    let formSelect = $('.form-select').eq(0);
    let secondSelect = $("#secondSelect");

    let shirtsSize = [90, 95, 100]
    let pantsSize = [28, 29, 30, 32]
    
    formSelect.on('input', function() {
      let value = this.value;
      
      if (value == '셔츠') {
        secondSelect.html("");
// for 반복문 사용 방법
        for (let i = 0; i < shirtsSize.length; i++) {
          document.querySelector('#secondSelect').insertAdjacentHTML('beforeend', `<option>${shirtsSize[i]}</option>`);
        }
        secondSelect.removeClass('selectHidden');
      } else if (value == '바지') {

        secondSelect.html("");
        secondSelect.removeClass('selectHidden');
// forEach 반복문 사용 방법
        pantsSize.forEach(function(a){
          secondSelect.append(`<option>${a}</option>`)
      } else {
        secondSelect.addClass('selectHidden');
      }
    });
```

#### object 자료 다룰 때 for in 반복문 가능
```js
    let obj = {name: 'kim', age:20}
    
    for (let key in obj){
      console.log(key);
      console.log(obj[key]);
    }
```

```ad-tip
**그래서 반복문의 용도는 2개가 있는데**
1. 코드복붙하고싶으면(동일한 코드 반복)
2. array, object 자료 다 꺼내고 싶을 때 
```

#### arrow function 문법
```js
var pants = [28, 30, 32];
pants.forEach(function(a){
  console.log(a)
});

pants.forEach((a) => {
  console.log(a)
});
```

#####  arrow function 심화
```js
// 예시1
pants.forEach( a => {
  console.log(this)
});

// 예시2
let 함수 = function(){ console.log('안녕') }
let 함수 = () => { console.log('안녕') }
```
- (예시1)
	- arrow function은 **파라미터가 하나면 () 소괄호 생략**해도 봐줍니다. 
	- 함수 중괄호 안에 return 한 줄 밖에 없으면 { } 중괄호와 return 동시에 생략해도 봐줍니다.
		- 👉 간결하니 콜백함수에 자주 사용됨

```ad-caution
- **그냥 함수와 arrow function의 기능차이**
- 함수 안에서 this를 써야할 경우 

	- 그냥 함수는 함수 안에서 this를 알맞게 재정의해줍니다.
	- arrow function은 함수 안에서 this를 재정의해주지 않고 바깥에 있던 this를 그대로 씁니다.

- 👉 그래서 이벤트리스너 콜백함수안에서 this를 써야하면 arrow function 쓰면 의도와 다르게 동작할 수도 있습니다. ==그런데선 쓰지마십시오== 
```


### array, for 반복문 실력향상 과제
```ad-question
- Q. Array에서 철수라는 자료를 찾고 싶습니다
	- array에서 이름을 찾아주는 함수를 만들고 있습니다.
	- 함수 안에 파라미터로 이름을 집어넣으면
	- 그 이름이 출석부에 있으면 콘솔창에 출력해주는 함수를 만들어봅시다. 
	- 어떻게 만들면 될까요? 

	 ```js
	var 출석부 = ['흥민', '영희', '철수', '재석'];
	
	function 이름찾기(){
	  //여기다 코드 짜십쇼 
	}
	```

- 동작 예시 :
	- 이름찾기('철수'); 라고 쓰면 콘솔창에 '있어요'라는 글자가 떠야합니다.
	- 이름찾기('명수'); 라고 쓰면 콘솔창에 아무 글자도 뜨지 않아야합니다.

- (조건) 이상한데서 찾아온 find, indexOf 같은 자바스크립트 기본함수들 사용금지 
```

```js
var 출석부 = ['흥민', '영희', '철수', '재석'];

function nameSeek(name){
  
  출석부.forEach((a) => {
    if (name == a){
      console.log("있어요")
    }
  });
}
```

```js
var 출석부 = ['흥민', '영희', '철수', '재석'];

function nameSeek(name){
  
  for(let i = 0; i <= 출석부.length; i++){
    if (name == 출석부[i]){
      console.log('있어요!');
      return 0
    }
  }
}
```

```ad-question
Q. 갑자기 구구단을 콘솔창에 출력하고 싶습니다.

철수는 구구단을 외우지 못하는 관계로

자바스크립트를 이용해 구구단을 2단부터 9단까지 콘솔창에 출력하고 싶어졌습니다.

빨리 출력해보십시오. 
```

```js
for(let i = 2; i <= 9; i++){
  
  for(let j = 1; j <= 9; j++){
    console.log(`${i} x ${j} = ${i*j}`)
  }
}

```


```ad-question
Q. 평균점수 계산기 만들기 

 

어떤 함수에 

기존 모의고사 성적들을 array 자료에 전부 담아 첫 파라미터로 입력하고 

이번 11월 모의고사 성적을 둘 째 파라미터로 입력하면  

11월 성적이 기존 성적들의 평균에 비해 얼마나 우수한지 결과를 알려주고 싶습니다. 

어떻게 함수를 만들면 될까요?

 

동작예시 :

함수([10, 20, 30, 40, 50], 40) 이렇게 쓰면 콘솔창에 "평균보다 10점이 올랐네요"가 떠야합니다. (평균이 30이니까)

함수([40, 40, 40], 20) 이렇게 쓰면 콘솔창에 "평균보다 20점이 떨어졌네요 재수추천"이 떠야합니다. (평균이 40이니까)
```

```js
function exam(arr, score){
  let lastSem = arr;
  
  let total = 0;
  for(let i = 0; i <lastSem.length; i ++){
    total += lastSem[i];
  }
  avgTotal = total/lastSem.length;
  
  if (score > avgTotal){
    console.log(`평균보다 ${score-avgTotal}점이 올랐네요`);
  } else{
    console.log(`평균보다 ${avgTotal-score}점이 떨어졌네요. 재수추천`);
  }
}
```

### Ajax 1 : 개념정리

#### 서버란?
- 유저가 데이터달라고 요청을 하면 데이터를 보내주는 간단한 프로그램일 뿐입니다.
- 서버에 데이터를 요청할 때는
	1. 어떤 데이터인지 url로 잘 기재해야하고
	2. 어떤 방법으로 요청할지 결정해야 (GET/POST 등)
- 데이터를 보내줍니다. 

#### GET/POST 요청하는 법?
- GET요청은 서버에 있던 데이터를 읽고싶을 때 주로 사용하고
- POST요청은 서버로 데이터를 보내고 싶을 때 사용합니다.
	- (실은 PUT, DELETE 요청도 있긴 합니다.)

- POST요청을 날리고 싶으면 `<form action="요청할url" method="post">` 태그 이용하면 됩니다. 그럼 폼이 전송되었을 때 POST요청을 날려줍니다. 
	- 👉 근데 GET, POST 요청을 저렇게 날리면 단점이 뭐냐면 **브라우저가 새로고침**됩니다.

#### AJAX란? 
- 서버에 GET, POST 요청을 할 때 새로고침 없이 데이터를 주고받을 수 있게 도와주는 간단한 브라우저 기능을 AJAX라고 합니다. 

#### jQuery로 AJAX요청하기
```js
$.get('https://codingapple1.github.io/hello.txt');

// 받아온 데이터 출력하기
$.get('https://codingapple1.github.io/hello.txt')
.done(function(data){
  console.log(data)
});

// post 방식으로 데이터 요청하기
$.post('url~~', {name : 'kim'})
```

```js
$.get('https://codingapple1.github.io/hello.txt')
  .done(function(data){
    console.log(data)
  })
  .fail(function(error){
    console.log('실패함')
  });
```
- `done` → ajax 요청 성공시 `.done` 안에 있는 코드를 실행해줍니다.
- `fail` → ajax 요청 실패시 `.fail` 안에 있는 코드를 실행
	- done/fail 말고 then/catch 써도 됩니다.

#### 쌩자바스크립트는 fetch 이런거써서 AJAX 요청가능
```js
fetch('https://codingapple1.github.io/price.json')
  .then(res => res.json())
  .then(function(data){
    console.log(data)
  })
  .catch(function(error){
    console.log('실패함')
  });
```
- fetch 함수는 Edge 브라우저 이상에서만 동작합니다. (브라우저 기본 함수)
- 근데 코드가 한 줄 더 필요한 이유가 뭐냐면, 서버와 데이터를 주고받을 때는 **문자만 주고받을 수 있습니다**. → 때문에 JSON 자료를 다시 array/object 자료로 바꿔주기 위해서.

```ad-tip
- jQuery의 $.get() 이런건 JSON으로 자료가 도착하면 알아서 array/object 자료로 바꿔줍니다.

- 기본함수 fetch() 이런건 JSON으로 자료가 도착하면 알아서 array/object 자료로 바꿔주지 않습니다.

- 그래서 fetch() 로 가져온 결과를 array/object로 바꾸고 싶으면 res.json() 이런 코드 한 줄 추가하면 됩니다. 
```


```ad-todo
- 오늘의 숙제 : 
	- list.html로 돌아가서 상품목록 3개 만들었던 html 코드는 싹 지우고
	- 자바스크립트 코드짜서 상품목록 3개를 동적으로 생성해오십시오 
	- var products 안에 있던 데이터도 html에 잘 표기되어있어야합니다. 

	```html
	<div class="container">
	  <div class="row">
	
	      <div class="col-sm-4">
	        <img src="https://via.placeholder.com/600" class="w-100">
	        <h5>Card title</h5>
	        <p>가격 : 70000</p>
	      </div>
	
	  </div>
	</div> 
	```
```

```html
  <div class="container">
    <div class="row">


    </div>
  </div>

<script>
	    for (let i = 0; i < products.length; i++) {
      document.querySelector('.row').insertAdjacentHTML('beforeend',
        `<div class="col-sm-4">
          <img src="https://via.placeholder.com/600" class="w-100">
          <h5>${products[i].title}</h5>
          <p>가격 : ${products[i].price}</p>
        </div>`
      )
    }
</script>
```

```js
// forEach를 사용한 방법
    products.forEach((a) => {
      let templates = 
          `<div class="col-sm-4">
          <img src="https://via.placeholder.com/600" class="w-100">
          <h5>${a.title}</h5>
          <p>가격 : ${a.price}</p>
        </div>`;
      $('.row').append(templates);
    })
```


### Ajax 2 : 상품 더보기 버튼 만들기
```ad-todo
오늘의 응용문제

 

1. 더보기버튼을 2번째 누르면 7,8,9번째 상품을 더 가져와서 html로 보여주십시오

https://codingapple1.github.io/js/more2.json 여기로 GET요청하면 7,8,9번째 상품이 도착합니다.

 

 

힌트는 유저가 더보기버튼을 몇 번 눌렀는지를 어디 기록해놔야

내가 버튼 누를 때마다 어디로 GET요청할 지 판단할 수 있겠군요. 

그리고 그 다음 10,11,12번 상품은 없으니

버튼을 3번은 못누르게 버튼을 숨기거나 그래도 좋을듯요 

 

 

 

2. 유사한 코드가 발생하고 있습니다.

지금 코드를 잘 보면 forEach() 반복문을 2번 쓴 것 같은데 

이 코드들이 매우 유사해보입니다.

함수나 그런걸로 축약해보는 연습도 해보면 좋을 것 같군요 

 

 

힌트는 

함수로 축약할 때 안에 미지의 변수같은게 있으면 파라미터로 바꾸는게 좋다고 했는데

a, i 이런 변수는 이미 콜백함수에 의해 파라미터화가 되어있기 때문에 a, i는 신경안써도 될듯요
```

```js
    
    let moreBtnCounter = 0;
    
    $('#moreBtn').click(function(){
      
      moreBtnCounter += 1;
      
      if (moreBtnCounter == 1){
        $.get('https://codingapple1.github.io/js/more1.json')
        .done(function(data){        
          products = data

          makeCards();
        })
      } else if (moreBtnCounter == 2){
        $.get('https://codingapple1.github.io/js/more2.json')
        .done(function(data){        
          products = data

          makeCards();
          $('#moreBtn').css('display','none');
        })
      }
    })
    
    
    var products = [{
        id: 0,
        price: 70000,
        title: 'Blossom Dress'
      },
      {
        id: 1,
        price: 50000,
        title: 'Springfield Shirt'
      },
      {
        id: 2,
        price: 60000,
        title: 'Black Monastery'
      }
    ];

    function makeCards(){
      for (let i = 0; i < products.length; i++) {
        document.querySelector('.row').insertAdjacentHTML('beforeend',
          `<div class="col-sm-4">
            <img src="https://via.placeholder.com/600" class="w-100">
            <h5>${products[i].title}</h5>
            <p>가격 : ${products[i].price}</p>
          </div>`
        )
      }
    }
    
    makeCards();
```
- html 템플릿 만드는 코드를 함수화 하였고, 버튼 클릭시 마다 횟수를 기록해서 그에 따른 분기를 만듦


### array에 자주 쓰는 sort, map, filter 함수
#### array 정렬하는 법 sort()
- array 자료는 순서개념이 있다보니 정렬도 가능합니다.
- 그냥 문자 가나다순으로 정렬하려면 `.sort()` 붙이면 되는데 <br>**숫자정렬**은 이렇게 코드짜면 됩니다.
- ==`sort()` 함수는 원본을 변환 시킴! 주의해서 사용! ==
```js
var 어레이 = [7,3,5,2,40];

어레이.sort(function(a, b){
  return a - b
});

console.log(어레이); // [2, 3, 5, 7, 40]
```

```ad-tip
- 자바스크립트에서 숫자가 담긴 arr를 바로 sort 하면 **문자 기준**으로 정렬을 실시한다. 
	```js
	var arr = [7,3,5,2,40];
	
	arr.sort();
	
	console.log(arr); // [2, 3, 40, 5, 7]
	```
```

```ad-caution
- 자바스크립트에서의 sort()의 이해
	 ```js
	어레이.sort(function(a, b){
	  return a - b
	}); 
	```

1. a, b는 array 안의 자료들입니다.
2. return 오른쪽이 양수면 a를 오른쪽으로 정렬해줍니다.
3. return 오른쪽이 음수면 b를 오른쪽으로 정렬해줍니다.
4. 그리고 array 안의 자료들을 계속 뽑아서 a, b에 넣어줍니다. 

- 이렇게 동작해서 a - b 저렇게 쓰면 숫자순 정렬이 되는 것입니다. 
	- 예를 들면 a, b가 7과 3일 경우 7 - 3 하면 4가 남습니다.
	- 4는 양수죠? 그러면 7을 3보다 오른쪽으로 보내줍니다.
- 그래서 숫자 오름차순 (123순) 정렬이 완성되는 것입니다.
```

```ad-question
- Q. 그럼 array 안의 숫자 내림차순 (321순) 정렬은 어떻게 할까요?
```

```js
let arr = [-1, 4, 3, 5, 10, 200]

arr.sort(function(a,b){
  return b - a
});

console.log(arr) // [200, 10, 5, 4, 3, -1]
```

```ad-question
Q. 문자정렬과 문자역순정렬은 어떻게 할까요?

`var 어레이 = ['다', '가', '나'];`

이런 자료가 있을 때 가나다순, 다나가순 정렬은 각각 어떻게 할지도 고민해봅시다.
```

```js
let arr = ['가', '바', '나', '아', '다']

arr.sort();
console.log(arr); // ['가', '나', '다', '바', '아']

// 사전순으로 정렬
arr.sort(function(a,b){
  return a > b ? 1 : -1;
});
console.log(arr)


// 역순으로 정렬
arr.sort(function(a,b){
  return a > b ? -1 : 1;
});
console.log(arr) // ['아', '바', '다', '나', '가']
```


#### array에 자주 쓰는 filter 함수 
- array 자료에서 원하는 자료만 필터링하고 싶으면 filter 함수를 씁니다.
```js
var 어레이 = [7,3,5,2,40];

var 새어레이 = 어레이.filter(function(a){
  return 조건식
}); 
```
1. a라고 작명한건 array 에 있던 데이터를 뜻하고
2. return 우측에 조건식을 넣으면 조건식에 맞는 a만 남겨줍니다.
3. 그리고 filter는 원본을 변형시키지 않는 고마운 함수기 때문에 새로운 변수에 담아써야합니다. ↔ `sort()`는 원본을 변화 시킴


- filter 함수 활용
```js
var 어레이 = [7,3,5,2,40];

var 새어레이 = 어레이.filter(function(a){
  return a < 4
}); 
```
- **어디에 쓰지?**
	- 👉 이런거 응용하면 쇼핑몰에서 "6만원 이하 상품만 보기" 이런 필터기능도 만들 수 있는 것입니다.

#### array에 자주 쓰는 map 함수
- array 안의 자료들을 전부 변형하려면 map 함수를 씁니다.
```js
var 어레이 = [7,3,5,2,40];

var 새어레이 = 어레이.map(function(a){
  return 수식같은거
}); 
```
1. a라고 작명한건 array 에 있던 데이터를 뜻하고
2. return 우측에 변경될 수식같은걸 넣으면 됩니다. 
3. 그리고 map는 원본을 변형시키지 않는 고마운 함수기 때문에 새로운 변수에 담아써야합니다. 


- map 함수 활용
```js
var 어레이 = [7,3,5,2,40];

var 새어레이 = 어레이.map(function(a){
  return a * 4
}); 
```
- **어디에 쓰지?**
	- 👉 이런거 응용하면 쇼핑몰에서 "달러 -> 원화로 변환하기" 이런 기능도 만들 수 있겠군요.


```ad-todo
**오늘의 숙제 :**

**1. "상품명 다나가순 정렬" 버튼과 기능을 만들어오십시오.**

누르면 상품이 '다나가' 순으로 정렬되어야합니다.

**2. "6만원 이하 상품보기" 버튼과 기능을 만들어오십시오.** 

누르면 6만원 이하 상품만 보여야합니다. 

더보기버튼과 함께 동작하는지 안하는지는 신경안써도 됩니다.
```

```html
  <div class="container my-3">
    <button id='sortByName' class="btn btn-danger">이름 역순 정렬</button> 
  </div>

<script>
    
    // 이름 역순 정렬
    $('#sortByName').click(function(){
      products.sort(function(a,b){
       return a.title > b.title ? -1 : 1; 
      });
      
      $('.row').html('');
      
      makeCards(products);
      
    });
</script>
```

```html
  <div class="container my-3">
    <button id='filterByPrice' class="btn btn-danger">6만원 이하 제품</button> 
  </div>


<script>
    // 가격 제한 필터링
    $('#filterByPrice').click(function(){
      let productsByPrice = products.filter(function(a){
        return a.price < 60000
      });
      
      $('.row').html('');
      
      makeCards(productsByPrice);
    });
</script>
```


### sort, map, filter 상품정렬기능 숙제

#### 숙제1 하기 전 쉬운거부터 다나가순 정렬해보자 
```js
var 어레이 = ['가', '다', '나'];
어레이.sort(function(a, b){
  return 여기뭐써야함?
});
```

- sort 함수 작동원리는 
	- a, b는 array안에 있던 자료들임
	- return 우측이 양수면 a를 우측으로 보냄
	- return 우측이 음수면 b를 우측으로 보냄 
	- array 안의 자료를 다 끌고와서 a, b에 계속 넣어봄
- 이렇습니다.

- 위 코드에서 중요한건 **return 우측에 뭘 집어넣냐**는 건데 
	- 예를 들어서
		- (1) a, b가 '가', '다' 일 경우 return 우측에 양수가 들어가야 다나가순 정렬이 됩니다. 
		- (2) a, b가 '다', '나' 일 경우 return 우측에 음수가 들어가야 다나가순 정렬이 됩니다. 
		- (3) a, b가 '가', '나' 일 경우 return 우측에 양수가 들어가야 다나가순 정렬이 됩니다. 
		- ...
- 이렇게 대충 하나하나 대입해서 따져보면 규칙같은게 눈에 보이는군요. 
	- a < b 일 경우 return 우측에 양수가 들어가면 되고 
	- a > b 일 경우 return 우측에 음수가 들어가면 됩니다. 
- (자바스크립트는 문자끼리 부등호비교가 가능합니다. ㄱ보다 ㅎ 이게 더 큽니다.)

```js
var 어레이 = ['가', '다', '나'];
어레이.sort(function(a, b){
  if (a < b) {
    return 1 
  } else {
    return -1
  }
});

console.log(어레이)
```

- 자바스크립트 이름 역순 정렬 기능 만들기(예시)
```js
products.sort(function(a,b){
	if(a.title > b.title){
		return 1
	} else if (a.title == b.title) {
		return 0
	} else {
		return -1
	} 
});
```

#### arrow function 활용하기
```js
//일반함수
var newProduct = products.filter(function(a){
  return a.price <= 60000
}); 

//화살표함수
var newProduct = products.filter(a => a.price <= 60000);
```
- 이 경우 함수에 파라미터가 1개면 소괄호 생략이 가능합니다. 
- 함수 { } 안에 return 한 줄 밖에 없으면 중괄호와 return 동시에 생략가능합니다.

```ad-todo
응용1. 가나다순 정렬버튼?

응용2. `<input>`을 이용해 유저가 직접 가격을 입력해서 필터하는 기능?

응용3. 원래 순서대로 되돌리기 버튼과 기능을 만들고 싶으면?
```

```html

  <div class="container my-3">
    <button id='sortByName2' class="btn btn-danger">이름순 정렬</button> 
  </div>
  
  <form id="inputForm" class="container my-3">
    <input id='filterByInput' placeholder="가격대를 입력하세요"> 
    <button type='submit'>제출</button>
  </form>
  
  <div class="container my-3">
    <button id='sortByOrigin' class="btn btn-danger">원래대로</button> 
  </div>

<script>
    // 원래 순대로 정렬
    let productsOrigin = products;
    
    $('#sortByOrigin').click(function(){
      
      $('.row').html('');

      products.sort(function(a, b){
        return a.id - b.id
      });
      
      makeCards(productsOrigin);
      
      moreBtnCounter = 0;
      
      $('#moreBtn').css('display','block');
    })
    
    // input 값에 따른 필터링
    $('#inputForm').on('submit', function(e){
      e.preventDefault();
      let filterPrice = $('#filterByInput').val();
      
      let productsByPrice = products.filter(function(a){
        return a.price < filterPrice;
      });
      
      $('.row').html('');
      
      makeCards(productsByPrice);
    });
    
    // 이름순 정렬
    $('#sortByName2').click(function(){
      products.sort(function(a,b){
       return a.title > b.title ? 1 : -1; 
      });
      
      $('.row').html('');
      
      makeCards(products);
      
    });


</script>
```


### DOM이라는 용어 개념정리 & load 이벤트

#### DOM 이란?
- 자바스크립트는 HTML조작에 특화된 언어 → 어떻게 HTML을 조작할 수 있을까?
	- 자바스크립트가 HTML 조작을 하기 위해선 **HTML을 자바스크립트가 해석할 수 있는 문법으로 변환**해놓면 됩니다.

```html
<div style="color : red">안녕하세요</div>
```
- 브라우저는 이런 HTML을 발견하면 object 자료로 바꿔서 보관해둡니다.
	- 👉 구체적으로는 `var document = { }` 이런 변수를 하나 만들어서 거기 넣어줍니다.

```js
// 예시
var document = {
  div1 : {
    style : {color : 'red'}
    innerHTML : '안녕하세요'
  }
}
```
- 위 변수를 **document object**라고 부릅니다. (👉 Document Object Model)
	- 👉 **자바스크립트가 HTML에 대한 정보들 (id, class, name, style, innerHTML 등)을 object 자료로 정리한걸 DOM**이라고 부릅니다. 

#### 브라우저는 HTML 문서를 위에서 부터 읽으며 DOM을 생성한다.
```html
(html 파일)

<script>
  document.getElementById('test').innerHTML = '안녕'
</script>

<p id="test">임시글자</p>
```
- 위 코드가 에러가 나는 이유는, 아직 브라우저가 `test` 요소를 찾지 못했는데, 자바스크립트로 조작을 하려 하기 때문이다.
	- 👉 p태그에 대한 DOM이 아직 생성되지 않았다.

#### 혹은 자바스크립트 실행을 약간 나중으로 미루는 방법도 있다
```js
// jQuery
$(document).ready(function(){ 실행할 코드 })

// JS
document.addEventListener('DOMContentLoaded', function() { 실행할 코드 })
```
- 👉 **"이 코드는 HTML 전부 다 읽고 실행해주세요"** 라는 의미이다. 

```html

<script>
  document.addEventListener('DOMContentLoaded', function() { 
    document.getElementById('test').innerHTML = '안녕'
  })
</script>

<p id="test">임시글자</p>
```
- 이렇게 코드를 짜면 에러가 발생하지 않는다. 
	- 👉 최근에는 자바스크립트를 `<body>` 태그 끝나기 전에 작성하기 때문에 문제 없으나, 혹 중간에 스크립트를 짜야할 때 유용하게 쓰일 수 있다. 

#### load 이벤트리스너
```js
셀렉터로찾은이미지.addEventListener('load', function(){
  //이미지 로드되면 실행할 코드 
})
```
- load 라는 이벤트리스너를 사용하면 DOM 생성뿐만 아니라 _이미지, css, js파일이 로드가 됐는지도 체크가능_ 하다.
	- 근데 외부 자바스크립트 파일에 저걸 적어놓으면, 그 js 파일보다 이미지가 더 먼저 로드되는 경우도 있으니 이벤트 발생체크를 못하는 경우도 있을 수 있다.

```js
$(window).on('load', function(){
  //document 안의 이미지, js 파일 포함 전부 로드가 되었을 경우 실행할 코드 
});

window.addEventListener('load', function(){
  //document 안의 이미지, js 파일 포함 전부 로드가 되었을 경우 실행할 코드
})
```
- document에 포함된 이미지, CSS파일 등 모든것이 로드가 되었는지 체크해줍니다. 
	- 👉 ready 이런거랑 차이는 앞선 `.ready()`는 DOM 생성만 체크하는 함수인데, <br>이것보다 약간 더 나아가서 모든 파일과 이미지의 로드상태를 체크한다

### 장바구니 기능과 localStorage

#### 브라우저의 저장공간
![](assets/JS%20입문%203-5.png)

| 저장소 이름     | 특징                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------- |
| Local Storage   | key : value 형태로 문자, 숫자 데이터 저장가능 <br>**브라우저 재접속시 남아있음(반영구적)** |
| Session Storage | key : value 형태로 문자, 숫자 데이터 저장가능 <br>브라우저 끄면 날아감(휘발성)           |
| Indexed DB      | 크고 많은 구조화된 데이터를 DB처럼 저장가능, 문법 어려움                                 |
| Cookies         | 유저 로그인정보 저장공간                                                                 |
| Cache Storage   | html, css, js, img 파일 저장해두는 공간                                                  |
- Local Storage / Session Storage
	- 문자, 숫자만 key : value 형태로 저장가능하고 5MB까지만 저장가능합니다. 
- **Local Storage는 브라우저 재접속해도 영구적으로 남아있는데 Session Storage는 브라우저 끄면 날아갑니다.** 
	- 👉 유저가 브라우저 청소하지 않는 이상 반영구적으로 데이터저장이 가능합니다. 

#### 로컬스토리지 사용법
```js
localStorage.setItem('이름', 'kim') //자료저장하는법
localStorage.getItem('이름') //자료꺼내는법
localStorage.removeItem('이름') //자료삭제하는법
```
- 문자와 숫자만 저장 가능하다. 
- 수정하는 법은 없어서 꺼내서 수정하고 다시 저장하면 된다.

##### 세션스토리지 사용법
```js
sessionStorage.setItem('이름', 'kim') //자료저장하는법
sessionStorage.getItem('이름') //자료꺼내는법
sessionStorage.removeItem('이름') //자료삭제하는법
```

#### 로컬스토리지에 array/object 저장하려면
- array/object를 로컬스토리지에 저장하면 강제로 문자로 바꿔서 저장됩니다. (**JSON 활용**)
```js
var arr = [1,2,3];
var newArr = JSON.stringify(arr);

localStorage.setItem('num', newArr)
```
1. JSON.stringify() 안에 array/object 집어넣으면 JSON으로 바꿔줍니다. 그럼 문자취급받음
2. 그걸 localStorage에 저장하라고 코드짰습니다. 

```js
var arr = [1,2,3];
var newArr = JSON.stringify(arr);

localStorage.setItem('num', newArr)

//꺼내서 쓸 땐
var 꺼낸거 = localStorage.getItem('num');
꺼낸거 = JSON.parse(꺼낸거);
console.log(꺼낸거);
```
- JSON으로 저장했으니 꺼내도 JSON입니다.
	- 그래서 꺼낸걸 다시 array/object로 바꾸고 싶으면 JSON.parse() 안에 넣으면 됩니다. 

- array/object → JSON 변환하고 싶으면 `JSON.stringify()`
- JSON → array/object 변환하고 싶으면 `JSON.parse()`

```ad-todo
오늘의 숙제 : 

1. 카드하단 구매버튼추가하고 그거 누르면 누른 상품의 이름을 localStorage에 저장하기
![](assets/JS%20입문%203-6.png)
▲ 저장하는 형태는 자유지만 이렇게 array 안에 전부 저장해보는게 어떨까요.
구매 누를 때 마다 array에 항목이 저렇게 추가되도록 해봅시다.

(팁1) 내가 누른 요소의 형제요소를 찾는 법을 알아야될 수도 있겠군요 
(팁2) localStorage가 비어있을 때는 array를 추가하면 되겠지만<br>localStorage에 이미 뭐가 있을 때는 array를 수정해야합니다.

2. cart.html 같은 파일 하나 만들어서 (장바구니 페이지)

그 페이지 방문시 localStorage에 있던 상품명들을 꺼내서 전부 진열해서 보여주면 됩니다.

디자인 신경쓸 필요없이 상품명들만 전부 잘 보이면 성공입니다. 
```

- 참고 자료: [선택자 2 - 기본 선택자 (인접관계 선택자)](https://tragramming.tistory.com/59)

```js
    let cartExist = localStorage.getItem('cart')
    
    //localstorage에 저장
    $('.buy').click(function(e){
      
      
      if (cartExist){
        let cart = JSON.parse(localStorage.getItem('cart'));
        cart.push(e.target.closest('div').querySelector('h5').innerHTML);
        
        let newCart = JSON.stringify(cart);
        localStorage.setItem('cart', newCart);
      } else {
        
      
        let cart = [];
        
        cart.push(e.target.closest('div').querySelector('h5').innerHTML);
        let newCart = JSON.stringify(cart);
        localStorage.setItem('cart', newCart);
      }
      
      
    });
```

```html
 <div class="container">
   
 </div>
  
  
  <script>
    let products = JSON.parse(localStorage.getItem('cart'));
    
    products.forEach(function(e, i){
      
      $('.container').append(`<p>${products[i]}<p>`)
    });
    
  </script> 
```


### 장바구니 기능과 localStorage 숙제

#### 숙제1. 구매버튼누르면 상품명을 localStorage에 저장

```js
products.forEach(function(a, i){
  (생략)
  <h5>${products[i].title}</h5>
  <p>가격 : ${products[i].price}</p>
  <button class="buy">구매</button>
});

$('.buy').click(function(){
  var title = $(e.target).siblings('h5').text();
  console.log(title)
});
```
- 카드레이아웃 생성하는 코드에 `<button class="buy">구매</button>`  추가
- 구매버튼에 이벤트리스너 → 누르면 일단 위에 있는 가격도 출력
- jQuery함수인 `.siblings()` 는 내 형제요소를 찾아줍니다. 
	- (형제요소는 나랑 나란히 배치된 html 태그들)
- 쌩자바스크립트는 `e.target.previousElementSibling.previousElementSibling`

```js

$('.buy').click(function(){
  var title = $(e.target).siblings('h5').text();
  if (localStorage.getItem('cart') != null ){ 
  //비어있지 않으면 == 이미 구매한 항목이 있으면
    var 꺼낸거 = JSON.parse(localStorage.cart);
    꺼낸거.push(title);
    localStorage.setItem('cart', JSON.stringify(꺼낸거));
  } else {
    localStorage.setItem('cart', JSON.stringify([title]))
  }
});
```

```ad-todo
(응용)
1. 같은 상품은 중복으로 추가되지 않게하고 싶으면? 
상품을 추가하기 전에 상품명이 이미 localStorage에 있는지 검사하면 되겠군요

2. 아니면 같은 상품 구매 누르면 상품 갯수가 올라가게?
상품명을 localStorage에 저장시 갯수도 저장하면 됩니다.

[ '상품명a 2개', '상품명b 4개' ... ] 이렇게 저장해도 되겠지만 여러 정보를 한 곳에 넣고 싶으면 array/object 쓰면 됩니다.

[ {title : '상품명a', num : 2}, {title : '상품명b', num : 4}  ... ] 이렇게 저장해놓으면 편리할듯요
```

```js
// 응용 1
    let cartExist = localStorage.getItem('cart')
    
    //localstorage에 저장
    $('.buy').click(function(e){
      
      let title = e.target.closest('div').querySelector('h5').innerHTML
      
      
      if (cartExist){
        let cart = JSON.parse(localStorage.getItem('cart'));
          
        if (!cart.includes(title)){
          
            cart.push(title);

            let newCart = JSON.stringify(cart);
            localStorage.setItem('cart', newCart);
        }

        
      } else {
        
      
        let cart = [];
        
        cart.push(title);
        let newCart = JSON.stringify(cart);
        localStorage.setItem('cart', newCart);
      }
      
      
    });
```