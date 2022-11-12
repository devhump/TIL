```javascript
// 콘솔창에 출력
console.log("콘솔창에 출력")
```



- 요소를 만들어서 할당 -> 출력

  ```javascript
  // h1 요소(element)를 만들고
  const title = document.createElement('h1')
  // 텍스트를 추가하고
  title.innerText = 'JS 기초' 
  // 선택자로 body태그를 가져와서
  const body = document.querySelector('body')
  // body태그에 자식 요소로 추가
  body.appendChild(title)
  ```



- 선택자를 활용해 특정 요소를 선택하기

  ```html
  <body>
    <h1 id="title">JS 기초</h1>
    <h2>DOM 조작</h2>
    <p class="text">querySelector</p>
    <p class="text">querySelectorAll</p>
  ...
      <script></script>
  </body>
  ```

  ```javascript
  // 선택자를 활용해 선택할 때 
  // 하나를 선택한다. => querySelector
  // 모든 결과를 선택한다. => querySelectorAll
  
  // id 를 통한 선택
  console.log(document.querySelector('#title'))
  // <h1 id="title">JS 기초</h1>
  
  // class를 통한 선택
  console.log(document.querySelectorAll('.text'))
  // NodeList(2) [p.text, p.text]
  console.log(document.querySelector('.text'))
  // <p class="text">querySelector</p>
  ```



- 속성 생성 / 출력

  ```html
  <body>  
    <h1 class="red text-center my-5">안녕하세요</h1>
    <script>
      // a tag 조작
      const a = document.createElement('a')
      a.innerText = '실라버스'
      const body = document.querySelector('body')
      body.appendChild(a)
      a.setAttribute('href', 'https://syllaverse.com')
      console.log(a.getAttribute('href'))
  
      // h1 tag 조작 (클래스)
      const h1 = document.querySelector('h1')
      console.log(h1.classList)
    </script>
  </boby>
  ```

  

- 이벤트 처리

  ```html
  <body>
    <h1>이건 복습말고 느낌만..</h1>
    <button id="btn1">클릭</button>
    <input type="text">
  
    <script>
      // btn1
      const btn1 = document.querySelector('#btn1')
      // btn1이 클릭되면 함수실행
      btn1.addEventListener('click', function() {
        // h1 태그를 잡아서
        const h1 = document.querySelector('h1')
        // 클래스 blue를 토글하자. 
        h1.classList.toggle('blue')
      })
  
      // input
      const input = document.querySelector('input')
      input.addEventListener('input', function(e) {
        console.log(e.target.value)
      })
    </script>
  </body>
  ```

  

- JS 메소드 활용

  ```html
  <body>
    <script> 
      const fruits = ['딸기', '바나나', '멜론']
      // 1.
      fruits.forEach(function(fruit) {
        // 반복시키면서 뭐 할건지.........
        console.log(fruit)
      })
      // 익명('딸기', 0, ['딸기', '바나나', '멜론']) 
      // 익명('바나나', 1, ['딸기', '바나나', '멜론'])
      // 익명('멜론', 2, ['딸기', '바나나', '멜론'])
  
      // 1-1. 
      fruits.forEach(function(fruit, i, array) {
        console.log(fruit, i, array)
      })
      // 익명('딸기', 0, ['딸기', '바나나', '멜론']) 
      // 익명('바나나', 1, ['딸기', '바나나', '멜론'])
      // 익명('멜론', 2, ['딸기', '바나나', '멜론'])
  
      // 3. 
      const print = function(a) {
        console.log(a)
      }
      fruits.forEach(print)
  
  
      // 2. array function
      fruits.forEach( fruit => console.log(fruit) )
  
  
      const myObj = {
        name: 'tak'
      }
    </script>
  </body>
  ```

  

- event

  - 버튼(button)

    ```html
    <body>
      <button id="btn">버튼</button>
      <p id="counter">0</p>
      
      <script>
        // 초기값
       let countNumber = 0
    
        // ID가 btn인 요소를 선택
        const btn = document.querySelector('#btn')
        console.log(btn)
        // btn이 클릭 되었을 때마다 함수가 실행됨
        btn.addEventListener('click', function() {
          console.log('버튼 클릭!')
          // countNumber를 증가시키고
          countNumber += 1
          // id가 counter인의 내용을 변경 시킨다. 
          const counter = document.querySelector('#counter')
          counter.innerText = countNumber
        })
      </script>
    </body>
    ```

    