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

![](assets/JS%20입문%203%20(코딩애플).png)
- 👆 위와 같이 중괄호(`{}`) 로 시작하는 경우, 대부분 **object 자료형**이다.

![](assets/JS%20입문%203%20(코딩애플)-28.png)
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
![](assets/JS%20입문%203%20(코딩애플)-29.png)[^자료출처: 코딩애플]

2. **client-side rendering**
	- 서버가 비어있는 html과 데이터만 보내줌 <br>👉 그리고 자바스크립트를 이용해서 고객 브라우저안에서 html을 완성
![](assets/JS%20입문%203%20(코딩애플)-30.png)[^자료출처: 코딩애플]

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
![](assets/JS%20입문%203%20(코딩애플)-31.png)

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

- [ ] 응용2번 아직 안함 #todo
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

### position : sticky 활용하기
#### position : sticky 
(Edge 이상에서 사용가능)

- 스크롤이 되었을 때 화면에 고정되는 요소를 만들고 싶을 때 사용할 수 있는 CSS 속성입니다.
- `position : fixed` 는 항상 화면에 고정이 되는 요소를 만들 때 사용한다고 배웠었는데 이거랑 뭔 차이가 있냐면, <br>`position : sticky` 는 스크롤이 되어서 **이 요소가 화면에 나오면** 고정시킨다는 특성이 있습니다.

- 한번 위의 예제를 만들어보도록 합시다.

```html
<body style="background : grey; height : 3000px">

<div class="grey">
  <div class="image">
    <img src="appletv.jpg" width="100%">
  </div>

  <div style="clear : both"></div>
  <div class="text">Meet the first Triple Camera System</div>
    
</div>

</body>
```

```css
.grey {
  background: lightgrey;
  height: 2000px;
  margin-top: 500px;
}
.text {
  float: left;
  width : 300px;
}
.image {
  float: right;
  width : 400px;
  position: sticky;
  top: 100px;
}
```

![](assets/JS%20입문%203%20(코딩애플)-32.png)

- 이렇게 작성하면 검고 긴 화면에 텍스트와 이미지가 하나씩 보입니다.
- 이미지에 position : sticky를 주시면
	1. 스크롤이 되어서 이미지가 보이는 순간
	2. viewport의 맨 위에서부터 100px 위치에서 고정이 됩니다.
	3. 그리고 부모 박스를 넘어서 스크롤 되면 이미지도 같이 사라집니다.

```ad-attention
(주의점) position : sticky는
1. 스크롤을 할 만한 부모 박스가 있어야하고
2. top 등 좌표속성과 함께 써야 제대로 보입니다. 
아무튼 응용하면 남들과는 다른 레이아웃을 만들 수 있습니다. 
```


### 스크롤 위치에 따라 변하는 애니메이션 : Apple Music UI 만들기

#### 위 UI를 만들기 위해 일단 HTML을 준비합니다. 
```html
<div class="card-background">
  <div class="card-box">
    <img src="카드이미지1경로">
  </div>
  <div class="card-box">
    <img src="카드이미지2경로">
  </div>
  <div class="card-box">
    <img src="카드이미지3경로">
  </div>
</div>
```

```css
.card-background {
  height: 3000px;
  margin-top: 800px;
  margin-bottom: 1600px;
}

.card-box img {
  display: block;
  margin: auto;
  max-width: 80%;
}
.card-box {
  position: sticky;
  top: 400px;
  margin-top: 200px;
}
```

- 겁나 긴 배경에 카드를 세로로 3개 배치했고, <br>position : sticky를 이용해서 스크롤시 화면에 고정되게 만들었습니다. 
- 여기까지만 해도 나름 봐줄만 한데 예제처럼 _스크롤시 opacity가 점점 줄어드는 애니메이션도 첨가_ 해보도록 합시다. 

#### 스크롤 위치에 따라 opacity가 변하는 애니메이션 만들기
- (일단 예제를 보면 스크롤을 내릴 때 카드가 1. opacity가 변하고 2. 사이즈가 줄어듭니다. 일단 1번 opacity만 구현해보도록 합시다)
- 여태까지 한 애니메이션은 **one-way 애니메이션**이었습니다. <br>그냥 시작화면과 최종화면만 있었을 뿐인데, 지금은 스크롤 위치에 따라 **opacity가 0에서 1까지** ==무수히 많은 중간단계==가 존재합니다. 
- 이런 애니메이션을 어떻게 만들지 코드로 짜보도록 합시다. <br>그 전에 일단 HTML 하단에 자바스크립트를 빨리 작성해보십시오.
```js
$(window).scroll(function(){
    var 높이 = $(window).scrollTop();
    console.log(높이);
});
```
- 스크롤 애니메이션의 기본은 위와 같은 자바스크립트입니다. 많이 보던 "스크롤시 내부 코드를 실행해주세요~" 라는 코드입니다. 
- 내부 코드엔 _현재 창의 스크롤바 높이를 알려주는 (window).scrollTop();_ 이라는 함수를 써본 뒤에 콘솔창에 출력을 해보았습니다. 

#### 현재 창의 스크롤바 높이를 왜 출력해보는데여?
- 왜냐면 현재 스크롤바 높이에 따라 opacity가 변하니까 <br>스크롤바가 _어디까지 스크롤 되면 opacity가 0이고 어디까지 스크롤 되면 opacity가 1인지_ 찾고 싶어서 그런거지 별 이유는 없습니다.

![](assets/JS%20입문%203%20(코딩애플)-33.png)[^코딩애플]

- 그래서 콘솔창에 현재 스크롤바 높이를 출력하면서 측정해보았습니다. 
- 650px 쯤 스크롤하면 opacity를 1로,<br>900px 쯤 스크롤하면 opacity를 대충 0.5로,<br>1150px 쯤 스크롤하면 opacity를 0으로 설정하면 좋을 것 같습니다. 
- 이걸 코드로 표현해보도록 합시다. 

```js
$(window).scroll(function(){

  var 높이 = $(window).scrollTop();
  console.log(높이);
        
// 650~1150까지 스크롤바를 내리면,
// 첫째카드의 opacity 1~0으로 서서히변경해주셈
  $('.card-box').eq(0).css('opacity', ???);

});
```

- 스크롤바를 내릴 때, `$('.card-box').eq(0).css('opacity', ???);` 이렇게 코드가 동작하도록 설정했습니다. 
- 첫카드의 opacity를 ???로 변하게 해야되는데 ???는 0 이런 고정된 값으로 설정할 수 없을 것 같습니다. <br>???부분은 **"스크롤바높이가 650~1150이 될 때 1~0이 되는 가변적인 값"**이 되어야하겠죠? 
- 그래서 일단 미지의 변수인 y라고 표현합시다.

![](assets/JS%20입문%203%20(코딩애플)-34.png)


```js
$(window).scroll(function(){

  var 높이 = $(window).scrollTop();
  console.log(높이);

  var y = 미지의 변수;
  $('.card-box').eq(0).css('opacity', y);

});
```

**Q. "스크롤바높이가 650~1150이 될 때 1~0이 되는 가변적인 값"**인 미지의 변수 y를 구해보십시오.

#### 내가 수학전공도 아닌데 도대체 미지의 변수 y를 어떻게 구합니까?
1. 실은 "스크롤바높이가 650~1150이 될 때 1~0이 되는 가변적인 값" y는 중학교 때 배운적이 있습니다. 

- 그래프로 표현해보면 이렇습니다.
![](assets/JS%20입문%203%20(코딩애플)-35.png)
- 그림으로 표현해보면 이렇지 않습니까. 
- 높이가 650~1150 이렇게 변할 때 1에서 0이 되는건 저런 그래프로 표현할 수 있을 것 같습니다. (여기서 높이라는건 아까 출력해본 높이 변수입니다)
- 👉이걸 어려운 수학용어로 **1차함수**라고 부릅니다요.

2. 그럼 이걸 수식으로 표현해봅시다.

```
//수학시간
y = a * 높이 + b
```
- y에 대한 1차함수는 우리가 뭐 기울기 이런걸 모를 때 일단 ax+b 이런 식으로 표현할 수 있다고 배웠습니다.
- 그럼 a랑 b라는 미지수만 잘 구하면 y가 뭔지 알 수 있는거네요? <br>a는 전문용어로 기울기, b는 전문용어로 y절편이라고 합니다만<br>그건 너무 어려우니 우리는 대입법을 이용해보도록 합시다.

3. a,b를 구하는건 대입법을 이용합니다. 
	- 위의 함수는 높이가 650일 때 y가 1, 높이가 1150일 때 y가 0입니다.
```
//수학시간
1 = a * 650 + b
0 = a * 1150 + b 
```

- 그럼 이렇게 대입해봐도 맞겠죠? 
- 방정식이 두개고 미지수가 두개면 충분히 풀 수 있습니다. 
- 그래서 연습장에 방정식을 잘 풀어보시면

```
//수학시간
1 = a * 650 + b
0 = a * 1150 + b

a = -1/500
b = 115/50
```

- 이렇게 나옵니다. 분수를 약분하고 그런건 필요없습니다. 

```ad-tip
- 참고: [기울기와 절편 그리고 직선의 방정식](../z_others/기울기와%20절편%20그리고%20직선의%20방정식.md)
- 이해가 안된다면...
![](assets/JS%20입문%203%20(코딩애플)-14.png)
```

- 그럼 a와 b값을 아까 y를 표현하던 수식에 대입하면 

```js
//다시 자바스크립트 
var y = -1/500 * 높이 + 115/50
```

**그럼 y를 구했으니 아까 코드를 이렇게 업데이트 할 수 있겠군요**

```js
$(window).scroll(function(){

  var 높이 = $(window).scrollTop();
  console.log(높이);

  var y =  -1/500 * 높이 + 115/50;
  $('.card-box').eq(0).css('opacity', y);

});
```

- 스크롤바 내려보시면 opacity라는 값이 y에 의해서 결정됩니다. 
- y는 스크롤 높이가 변할 때마다 매번 바뀌기 때문에 아까와 같은 UI를 구현가능한 것입니다요. 
`
```ad-todo
숙제 : 투명도 뿐만 아니라 카드가 0.9배 정도로 서서히 작아지는 것도 똑같이 구현해봅시다.  

지금까지 카드 투명도가 서서히 변하는걸 구현해 봤는데

현재 창을 650~1150만큼 스크롤 했을 때 카드의 크기가 1에서 0.9로 작아지도록 만들어주시면 됩니다.

```

```js
// 답지보고 베낌 ㅠㅠ
var z = (-1/5000) * 높이 + 565/500;
$('.card-box').eq(0).css('transform', `scale( ${z} )`);
```
- 👉더 부드러운 동작을 원하시면 card-box라는 div에 `transition : all 0.2s` 같은걸 부여하면 됩니다.

```ad-tip
- 응용문제에서 추가로 2번에서 3번 사진 넘어갈 때에도 같은 효과를 부여하기 위해선 어떻게 코드 짜야 하는가 고민하다가, 강좌 게시판에서 다른 사람 코드를 찾았다. %%이분도 수치 계산이 어려워 chatGPT한테 물어봤다고...ㅋㅋ%%
	```js
	    var y2 = (-1 / 800) * 높이 + 115 / 50;
        $('.card-box').eq(1).css('opacity', y2);
        
        var z2 = (-1 / 5000) * 높이 + 2.25;
        $('.card-box').eq(1).css('transform', `scale( ${z} )`);
	```
- 높이쪽을 조절해야하나보다 하고 한참 고민했는데, 방정식 자체를 새로 짜야 하는 거더라...
- 참고로 두번째요소는 1000~1800 스크롤 값으로 잡았다고함.
```


### 캐러셀에 스와이프 기능 만들기
- 오늘은 예전에 만들었던 캐러셀 UI를 소환해서 여기에 터치 & 스와이프 기능을 만들어봅시다.

```html
<div style="overflow: hidden">
    <div class="slide-container">
      <div class="slide-box">
        <img src="car1.png">
      </div>
      <div class="slide-box">
        <img src="car2.png">
      </div>
      <div class="slide-box">
        <img src="car3.png">
      </div>
    </div>
</div> 
```

![](assets/JS%20입문%203%20(코딩애플)-36.png)[^코딩애플]
- 폭이 300vw인 큰 박스 안에 작은 이미지 3개가 이렇게 있는 레이아웃이었는데, 버튼을 누르면 박스 전체를 -100vw 만큼 움직이게 만들어서 캐러셀을 만들었습니다.

- 터치되는 캐러셀같은거 조작해보면 대충 이런 기능이 들어있습니다.
- **기능1.** 드래그한 거리만큼 사진도 왼쪽으로 움직여야함
- **기능2.** 마우스 떼었을 때 일정거리 이상 이동했으면 사진2 보여줌, 아니면 다시 사진1 보여줌

- 기능1 부터 만들어봅시다. 
	- 👉 근데 이거 만들려면 알아야할 이벤트가 3개 있습니다.

#### mouse 이벤트 3개
- 마우스로 어떤 html 요소를 조작할 때 발동하는 이벤트가 있습니다.

| 이벤트    | 설명                             |
| --------- | -------------------------------- |
| mousedown | 어떤 요소에 마우스버튼 눌렀을 때 |
| mouseup   | 어떤 요소에 마우스버튼 뗐을 때   |
| mousemove | 어떤 요소위에서 마우스 이동할 때 |

```html
<div>캐러셀있는곳</div>

<script>
  $('.slide-box').eq(0).on('mousemove', function(){
    console.log('안녕')
  })
</script>
```
- 그래서 예를 들어 이렇게 코드짜면 `.slide-box` 위에 마우스 움직일 때 마다 '안녕'이 출력됩니다.

```html
<div>캐러셀있는곳</div>

<script>
$('slide-box').eq(0).on('mousedown', function(e){
	console.log(e.clientX) // ← 현재 마우스 좌표 출력
})
</script>
```
- 이게 더 유용한데 mouse어쩌구 이벤트리스너안에선 `e.clientX`,  `e.clientY`를 출력해볼 수 있는데 **현재 마우스 좌표를 알려줍니다**. 
	- 👉 이거 쓰면 유저가 얼마나 사진을 드래그 했는지 그런 것도 알 수 있을듯 

#### 기능1. 사진1을 왼쪽으로 드래그한 거리만큼 사진1도 왼쪽으로 움직여야함
- 예를 들어 사진1을 클릭하고 왼쪽으로 50px 잡아끌었다면 *사진1도* 왼쪽으로 50px 움직여야합니다.
	- 👉 근데 사진1만 움직이는거말고 사진3개 전부 담긴 큰 박스 움직이는게 좋을듯

```ad-tip
- 이동거리 = **마우스 누를 때의 X좌표** - **마우스 움직일 때의 X좌표**
```

```html
<div>캐러셀있는곳</div>

<script>
  $('.slide-box').eq(0).on('mousedown', function(e){
    e.clientX // ← 이거랑
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    e.clientX // ← 이거를 빼야할듯
  });
</script>
```

```ad-attention
- 이동거리를 구하기 위해 두 개의 다른 함수 내에서 동일한 변수를 사용해야함
	- 👉 함수 바깥에 선언된 함수 ⇒ **전역변수**
```

```html
<script>
  var 시작좌표 = 0;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    console.log(e.clientX - 시작좌표)
  });
</script>
```

1. 시작좌표라는 변수를 함수들 바깥에 만들어둡니다. (그럼 모든 함수에서 이용가능)
2. 마우스 클릭시 현재 좌표를 `var 시작좌표`에 저장해줌
3. mousemove 이벤트발생시 `var 시작좌표`랑 현재좌표인 `e.clientX`를 빼봄
	- 👉 그걸 출력해보면 현재 드래그 이동거리가 잘 나오는군요

- 왼쪽으로 드래그하면 -100 이렇게 출력되고 오른쪽으로 드래그하면 100 이런거 출력되는듯  
- 이제 이동거리를 구했으니 "이동거리만큼 저거 박스도 이동해달라"고 코드짜오십시오.  

#### 이동거리만큼 저거 박스도 이동해달라
```html
<script>
  var 시작좌표 = 0;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    console.log(e.clientX - 시작좌표)
    $('.slide-container').css('transform', `translateX( ${e.clientX - 시작좌표}px )`)
  });
</script>
```
- 예전에 `translateX`를 조절하면 박스가 왼쪽으로 오른쪽으로 이동했었습니다.<br>그래서 그거 줬습니다. margin-left 이런거 줘도 되긴 할듯요 
- 근데 약간 반응이 느린 이유는 예전에 `.slide-container` 박스에 `transition : all 1s;` 이런걸 추가해서 그런가봅니다.
	- transition어쩌구 붙어있던 css 코드를 삭제하면 잘됩니다.

#### 왜 마우스 클릭도 안했는데 박스가 움직임?
- 오늘도 주인님이 시키는대로 하는 컴퓨터는 전혀 죄가 없습니다.<br>*"클릭하고나서만 박스 이동해달라"* 고 컴퓨터에게 명령을 주면 됩니다. 

```html
<script>
  var 시작좌표 = 0;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    if (마우스눌렀냐???) {
      $('.slide-container').css('transform', `translateX( ${e.clientX - 시작좌표}px )`)
    }
  });
</script>
```
- if문 추가하면 되는거 아닙니까<br>근데 마우스 눌렀는지 아닌지는 어떻게 판단하죠?
	- 👉 그건 다행히 `mousedown` 이벤트리스너가 있군요. 그 안에서 판단하면 될 것 같습니다.


```html
<script>
  var 시작좌표 = 0;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
    var 눌렀냐 = true;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    if (눌렀냐 === true) {
      $('.slide-container').css('transform', `translateX( ${e.clientX - 시작좌표}px )`)
    }
  });
</script>
```
1. 마우스 누르면 var 눌렀냐 변수를 true로 만들라고 코드짰습니다.
2. 그리고 if문에선 var 눌렀냐가 true일 때만 박스움직이라고 코드짰습니다.
- ==문제는 변수 `눌렀냐` 가 함수 내에 선언되어 있음
	- 👉 **전역변수로 선언하기!**

```html
<script>
  let 시작좌표 = 0;
  let 눌렀냐 = false;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
    눌렀냐 = true;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    if (눌렀냐 === true) {
      $('.slide-container').css('transform', `translateX( ${e.clientX - 시작좌표}px )`)
    }
  });
</script>
```

#### 왜 마우스 뗐는데도 아직 박스가 움직임?
- 컴퓨터에게 내 뜻대로 작동하라고 기대만 하면 안되고 여러분이 하나하나 명령내려주셔야합니다. *"마우스 떼었을 때는 박스 움직이지 말라"* 고 컴퓨터에게 명령을 내립시다. 
- 알아서 해봅시다. 

```html
<script>
  let 시작좌표 = 0;
  let 눌렀냐 = false;

  $('.slide-box').eq(0).on('mousedown', function(e){
    시작좌표 = e.clientX;
    눌렀냐 = true;
  });

  $('.slide-box').eq(0).on('mousemove', function(e){
    if (눌렀냐 === true) {
      $('.slide-container').css('transform', `translateX( ${e.clientX - 시작좌표}px )`)
    }
  });
    
  $('.slide-box').eq(0).on('mouseup', function(e){
    눌렀냐 = false;
    
  });
</script>
```


```ad-tip
- 이미지 드래그 안 되게 하는 방법
	```html
	  <div style="overflow: hidden">
	    <div class="slide-container">
	      <div class="slide-box">
	        <img src="car1.png" draggable="false"> <!-- 드래그 금지 -->
	      </div>
	      <div class="slide-box">
	        <img src="car2.png" />
	      </div>
	      <div class="slide-box">
	        <img src="car3.png" />
	      </div>
	    </div>
	  </div>
```


```ad-todo
- 오늘의 숙제 : 
	- 기능2 만들어옵시다.
	- 마우스 떼었을 때 일정거리 이상 이동했으면 사진2 보여줌, 아니면 다시 사진1 보여줌
```



### 캐러셀에 스와이프 기능 만들기 숙제 & 터치이벤트

#### 기능2. 마우스 떼었을 때 이동거리가 100 이상이면 2번사진 보여주기
- 이거는 마우스를 떼면 실행할 기능이니까 mouseup 이벤트리스너안에 코드짜면 되겠군요.
	- 그래서 if 사용해서 코드짜봤습니다.
```html
<script>
  (생략)

  $('.slide-box').eq(0).on('mouseup', function(e){
    눌렀냐 = false;

    if (이동거리 100이상) {
      2번사진보여주셈 
    } else {
      1번사진보여주셈
    }
  });
</script>
```

```html
<script>
  (생략)

  $('.slide-box').eq(0).on('mouseup', function(e){
    눌렀냐 = false;

    if (e.clientX - 시작좌표 < -100) {
      $('.slide-container').css('transform', 'translateX(-100vw)');
    } else {
      $('.slide-container').css('transform', 'translateX(0vw)');
    }
  });
</script>
```


#### 근데 마우스 떼면 왜 사진이 순간이동함 
- 마우스 떼면 2번사진으로 이동하라고 코드짰기 때문입니다. 서서히 이동하는 애니메이션 추가는 안했으니까요. 애니메이션주고 싶으면 이동할 박스에 `css transition` 추가하면 됩니다.

- 근데 문제가 있는데 이전 강의에서 기능1 만들 때 불편해서 `.slide-container` 박스에 있던 **transition을 제거**했습니다. 왜냐면 누르고 사진을 스와이프할 때는 transition이 있으면 느리게 동작했으니까요.

- 그래서 평소엔 transition이 필요가 없는데 *사진에서 마우스를 떼면 transition이 필요*합니다. 그럼 *"마우스 떼면 잠깐 0.5초정도 transition 붙였다가 떼주세요"* 라고 코드짜면되지않을까요?
- 👉 예전에 배운 타이머같은거 활용하면 가능합니다. transition 붙여놓고 0.5초 후에 떼라고 하면 됩니다. 

```html
<script>
  (생략)

  $('.slide-box').eq(0).on('mouseup', function(e){
    눌렀냐 = false;

    if (e.clientX - 시작좌표 < -100) {
      $('.slide-container').css('transition', 'all 0.5s').css('transform', 'translateX(-100vw)');
    } else {
      $('.slide-container').css('transition', 'all 0.5s').css('transform', 'translateX(0vw)');
    }
    setTimeout(()=>{
      $('.slide-container').css('transition', 'none')
    }, 500)
    
  });
</script>
```

1. 마우스 떼면 transition : all 0.5s 이거 부착하라고 코드짰습니다.<br>jQuery는 저렇게 점찍고 계속 추가할 수 있습니다. 쌩자바스크립트는 변경사항이2개면 2줄 작성하면 됩니다.
2. 그리고 setTimeout 이용해서 0.5초 후에 transition : none을 주라고 코드짰습니다. 그럼 아까 한글로 설명했던거 구현 끝

#### 모바일은 터치 이벤트리스너 달아야함 
![](assets/JS%20입문%203%20(코딩애플)-37.png)
- 사이트를 모바일기기로 테스트하고 싶으면 크롬개발자도구 좌상단 toggle device toolbar 버튼누르면 됩니다. 근데 모바일기기로 테스트해보면 스와이프가 안됩니다. 왜냐면 마우스이벤트리스너를 달아놨기 때문입니다. *모바일은 터치이벤트리스너를 달아줘야 터치에 반응*합니다.

| 이벤트     | 설명                  |
| ---------- | --------------------- |
| touchstart | 터치시작시 발동       |
| touchmove  | 터치중일 때 계속 발동 |
| touchend   | 터치종료시 발동       |

```html
<script>
  $('.slide-box').eq(0).on('touchstart', function(){
    시작좌표 = e.touches[0].clientX;
    생략
  })

  $('.slide-box').eq(0).on('touchmove', function(){
    생략
  })

  $('.slide-box').eq(0).on('touchend', function(){
    생략
  })

</script>
```

- 기존 코드를 이렇게 바꾸면 됩니다. 그럼 모바일에서도 아까랑 똑같이 동작하는데 주의사항은 _e.clientX를 **e.touches[0].clientX** 이걸로 바꾸면_ 됩니다. 왜냐면 터치는 여러 손가락으로 할 수 있어서 그 중 몇번째 손가락인지 지정해줘야합니다. _touchend 이벤트리스너에선 e.clientX 말고 **e.changedTouches[0].clientX** 쓰면 됩_ 니다. 

- Q. 어 그럼 PC환경에서는 안되는데요?
	- 👉 그럼 기존걸 touch로 바꾸는게 아니라 touch 이벤트리스너3개를 하단에 추가하면 됩니다.

```ad-tip
##### 아 코드 너무 기네 
-  자바스크립트는 외부 라이브러리 의존도가 언제나 높은데 그중 **Hammer.js** 라이브러리를 사용하면 조금 쉽게 기능 개발이 가능하다.
	- 브라우저 호환성도 알아서 잡아주고
	- 이벤트리스너 6개대신 1개만 써도 되고 
	- 스와이프, pinch, rotate 등 여러 제스쳐를 감지하는 이벤트리스너 제공해서 편리
```

#### 그래서 오늘 집에 가져갈 내용은 
- 그래서 오늘 집에 가져갈 내용은 *"아 캐러셀 스와이프기능만들려면 변수2개, 이벤트리스너 3개부터 만들고 시작하면 되는구나"* 가 아닙니다.
	1. 유저의 터치를 여러방식으로 감지할 수 있구나~
	2. 터치좌표, 터치이동거리도 출력해볼 수 있구나 
	- 이것만 잘 알아가면 되겠습니다. 

```ad-attention
- 오늘도 코드만 따라쳤다면 지우고 1주 후에 다시 답보지말고 만들어봅시다.
- 이상한 변수 10개와 이벤트리스너부터 만들어야되는게 아니라 
	1. 구현하고 싶은 기능과 동작방식을 한글로 상세히 설명부터 하고
	2. 작고 쉬운 것 부터 개발해나가면 됩니다.
```

```ad-todo
응용1. 나머지 2번 3번 사진도 스와이프 가능하게 만들어봅시다.

응용2. 첫 사진을 우측으로 스와이프 못하게 막으려면? 아마 if문 추가하면 될 수도 있겠군요

응용3. 제 코드만 따라쳤다면 싹 지우고 1주 후에 가물가물할 때 답보지 말고 직접 만들어봅시다.
```

```js
// 응용 1번번

/////////////////////carousel  2번////////////////////////////////////
      let 시작좌표2 = 0;
      
      $(".slide-box")
        .eq(1)
        .on("mousedown", function (e) {
          시작좌표2 = e.clientX + 시작좌표;
          눌렀냐 = true;
        });
    
      $(".slide-box")
        .eq(1)
        .on("mousemove", function (e) {
          if (눌렀냐 === true) {
            $(".slide-container").css(
              "transform",
              `translateX( ${e.clientX - 시작좌표2}px )`
            );
          }
        });

      $(".slide-box")
        .eq(1)
        .on("mouseup", function (e) {
          눌렀냐 = false;

          let mouseMove = e.clientX - 시작좌표2;

          if (mouseMove < -100) {
            $(".slide-container")
              .css("transition", "all 0.5s")
              .css("transform", "translateX(-200vw)");
            
          } else {
            $(".slide-container")
              .css("transition", "all 0.5s")
              .css("transform", "translateX(-100vw)");
          }
        
          setTimeout(()=>{
            $('.slide-container').css('transition', 'none')
          }, 500)
        });

/////////////////////carousel  3번////////////////////////////////////
      let 시작좌표3 = 0;
      
      $(".slide-box")
        .eq(2)
        .on("mousedown", function (e) {
          시작좌표3 = e.clientX + 시작좌표2;
          눌렀냐 = true;
        });
    
      $(".slide-box")
        .eq(2)
        .on("mousemove", function (e) {
          if (눌렀냐 === true) {
            $(".slide-container").css(
              "transform",
              `translateX( ${e.clientX - 시작좌표3}px )`
            );
          }
        });

      $(".slide-box")
        .eq(2)
        .on("mouseup", function (e) {
          눌렀냐 = false;

          let mouseMove = e.clientX - 시작좌표3;

          if (mouseMove < -100) {
            $(".slide-container")
              .css("transition", "all 0.5s")
              .css("transform", "translateX(0vw)");
            
          } else {
            $(".slide-container")
              .css("transition", "all 0.5s")
              .css("transform", "translateX(-300vw)");
          }
        
          setTimeout(()=>{
            $('.slide-container').css('transition', 'none')
          }, 500)
        });
```
- 처음에 1 → 2번은 쉽게 되는데, _그 이후로는 왜 안 움직이지??_ 한참을 고민했다.<br>처음부터 되짚어보며, 겨우 생각해 냈고,
- 그 이후엔 왜 꼬이지?? _(왜 2번을 드래그 하는데, 1번으로 순간이동을...)_ 하고 고민하다가 좌표값 갱신을 생각해냄.

```js
// 응용 2번
      $(".slide-box")
        .eq(0)
        .on("mousemove", function (e) {
          
        
          if (눌렀냐 === true && e.client > 0) {
  
            $(".slide-container").css(
              "transform",
              `translateX( ${e.clientX - 시작좌표}px )`
            );
          }
        });
```


### 간혹 쓰는 Switch 문법

```ad-tip
- **if문과 switch의 차이**
	- if는 다양한 조건식 가능
	- switch는 변수 1개만 테스트 가능 
		- 👉  대신 switch가 더 깔끔해보임
```

default
break

#### switch 사용법
```js
let 변수 = 2 + 2;

switch (변수){
  case 3 :
    alert('변수가 3이네요');
    break
  case 4 :
    alert('변수가 4네요');
    break
}
```

- switch의 소괄호엔 조건식이 아니라 **검사해볼 변수**를 넣으면 됩니다. 
- 그리고 _변수가 3일 때 코드 실행해주세요~_ 라고 코드짜고 싶으면 case 문법 저렇게 사용하면 됩니다.
- 그리고 코드실행을 끝내고 싶으면 `break`라는걸 추가해주면 됩니다. 그럼 switch 중괄호를 탈출해줍니다.

```js
let 변수 = 2 + 5;

switch (변수){
  case 3 :
    alert('변수가 3이네요');
    break
  case 4 :
    alert('변수가 4네요');
    break
  default : 
    alert('다 아니네')
}
```

- else같은걸 쓰고 싶으면 `default :` 추가해주면 됩니다.<br>그러면 case에 해당되는게 하나도 없을 때 안에 있는 코드를 실행해줍니다.

#### 그래서 배운 기념으로 간단한 심리테스트 게임
```html
<div id="quiz">
  <h4>물에 빠지면 누구먼저 구할 것임?</h4>
  <button>와이프</button>
  <button>부모님</button>
  <button>키우던 개</button>
</div>

<script>
  document.querySelector('#quiz').addEventListener('click', function(e){
    switch (e.target.innerHTML){
      case '와이프':
        alert('와이프를 좋아하시네요');
        break
      case '부모님':
        alert('효자네요');
        break
      case '키우던 개':
        alert('역시 사람보단 동물이 더 낫죠');
        break
    }
  });

</script>
```
- 👉 이런 식으로 변수 하나의 값에 따라서 각각 다른 기능을 실행하고 싶을 때 쓰면 깔끔해보일 수 있습니다.

### (실전) 웹개발 기능대회 예제
- 전국기능경기대회 있는데 기술진흥원에서 매년 이런 주제로 대회를 개최하고 시상합니다.
![](assets/JS%20입문%203%20(코딩애플)-38.png)

![](assets/JS%20입문%203%20(코딩애플)-39.png)

**Q1. 만들 HTML파일은 위 사진과 비슷한 레이아웃을 구성해야합니다.** 
- 디자인 잘했는지 평가는 안하니 Bootstrap 사용하면 빠를듯
- 상품목록은 .json 파일로 제공되는데 **그 파일에 있는 데이터를 박아넣으셔야합니다.**
- ajax get 요청으로도 로컬 json파일에 있는 데이터를 가져올 수 있습니다.

![](assets/JS%20입문%203%20(코딩애플)-40.png)

**Q2. 상품 검색 기능이 필요합니다.**
- 상단 `<input>`에 검색어를 입력하면 그 글자가 제목, 업체명에 들어있으면 그 상품만 보여줘야합니다. 
- 찾은 글자에 노란색 배경을 입혀보는 것도 좋겠군요

![](assets/JS%20입문%203%20(코딩애플)-41.png)

**Q3. 위 사진 처럼 장바구니로 상품을 드래그할 수 있게 만들어야합니다.** 
- 상품을 드래그해서 검은 박스에 놓으면 카드가 하나 생성됩니다.
- 담기버튼눌러도 똑같이 카드 생성해주면 됩니다.
- 이미 있는 상품이면 카드생성이 아니라 수량만 1 증가해야합니다.

![](assets/JS%20입문%203%20(코딩애플)-42.png)

**Q4. 나머지는 별거 아니고** 
- 장바구니 개별 항목의 주문 수량을 변경할 수 있어야합니다.
- 모든 상품과 수량의 최종 합계 금액을 어딘가 보여주어야합니다. 
- 구매하기를 누르면 성함 연락처를 입력할 수 있는 모달창을 띄워주어야합니다.

![](assets/JS%20입문%203%20(코딩애플)-43.png)

**Q5. 모달창에서 구매완료 누르면 영수증을 이미지형태로 보여줘야합니다.**
- 1. 현재 날짜 2. 주문한 모든 상품명 & 가격 3. 총 합계금액이 나오면 됩니다.
- 이미지 만드는건 별거 아니고 `<canvas>`라는 태그를 이용합니다. 
- 자바스크립트쓰면 `<canvas>`안에 사진넣고텍스트 입력도 가능합니다.