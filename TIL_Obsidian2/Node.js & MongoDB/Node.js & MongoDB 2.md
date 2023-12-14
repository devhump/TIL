### 글 작성기능 만들기 1 (POST 요청)

- 글쓰기 기능을 만들어볼건데<br>알아서 한번 코드 짜보시면 되겠습니다. 

- 안배운건데 코드를 어떻게 짜냐고요?<br>첨보는 기능하나 만들라고 했을 때 어떻게 해야되냐면 
	1. 기능이 어떻게 동작하는지 한글로 상세히 정리부터 하고
	2. 그걸 코드로 번역하기  
- 이렇게 하면 처음보는 기능도 알아서 잘 만들 수 있습니다. <br>숙련된 프로그래머들도 다들 이렇게 합니다. 

%%자바스크립트 기초강의에서 맨날 연습하던 것임%%

### 글작성 기능이 어떻게 동작하는지 정리부터
- 글작성 기능은<br>유저가 작성한 글을 DB에 저장하면 그게 글쓰기 기능 끝아니겠습니까<br>이렇게 써놓고 그대로 코드로 번역만 하면 될거같은데 <br>이렇게 코드짜면 금방 서비스 종료한다고 했습니다. 

- 유저가 DB와 직접 통신하게 냅두면 유저가 DB에 이상한 짓을 할 수도 있기 때문에<br>DB조작이 필요한 경우는 **중간에 서버를 거치는 식으로** 코드짜는게 좋습니다 
	1. **유저가 글작성페이지에서 글을 작성해서 서버로 글을 보내고** 
	2. **서버는 글을 받으면 잘썼나 확인해보고** 
	3. **서버는 그걸 DB에 저장**
- 이러면 될거같습니다 

- 그럼 이거 그대로 코드로 번역만 하면 구현 끝입니다.<br>그리고 모르는 내용이 나오면 구글 검색하면 되는 것임

### write.ejs 글작성 페이지 만들기
- 1번기능을 만들어볼건데 그러기 위해서 유저가 글을 작성할 수 있는 html 페이지부터 만들어봅시다.<br>ejs파일로 하나 만들면 좋을거같아서 write.ejs 파일 하나 만들었고 <br>안에 글작성할 수 있는 폼을 만들면 되겠군요. 

#### write.ejs 레이아웃
```html
<form class="form-box">
    <h4>글쓰기</h4>
    <input>
    <input>
    <button type="submit">전송</button>
</form> 
```

```css
input,div {
  box-sizing: border-box;
}
.form-box {
  background : white;
  padding : 25px;
  margin: 20px;
  border-radius: 8px;
}
.form-box input {
  padding : 10px;
  font-size: 16px;
  width: 100%;
  border: 1px solid black;
  border-radius: 5px;
  margin-bottom: 10px;
}
.form-box button {
  padding: 10px;
  border : none;
  background : lightgrey;
  border-radius: 5px;
}
```

- 잠깐 설명하자면
	- 웹페이지에서 뭔가 작성할 수 있는 인풋을 만들고 싶으면 `<form>` 안에 `<input>` 을 쓰면 됩니다 
	- `<input type=" ">` type속성 안에 다양한걸 집어넣어서 다양한 인풋을 만들 수 있음  
	- 전송 버튼은 `type="submit"` 속성을 넣은 `<button>` 만들면 됩니다. 

### 버튼누르면 서버로 글 전송하기
- 그럼 서버로 작성한 글을 전송하면 되는데<br>어떻게 전송하냐면 POST요청을 사용하면 쉽게 전송이 가능합니다. 

- 서버에 뭔가 요청하려면 정확히 URL과 method를 기입하랬습니다. <br>그래서 실은 `<form>`태그에도 URL과 method 기입란이 있는데 

```html
(write.ejs 중)

<form action="/어쩌구" method="POST">
```

- action 속성열어서 /url 채우고 <br>method 속성을 열어서 POST라고 채우면 <br>이제 폼태그안에있던 전송버튼누르면 /어쩌구 URL로 POST요청이 갑니다.<br>편리하죠?

```html
(write.ejs 중)

<form class="form-box" action="/add" method="POST">
   <h4>글쓰기</h4>
    <input name="title">
    <input name="content">
    <button type="submit">전송</button>
</form> 
```

- 근데 이렇게만 하면 `<input>`안에 유저가 적은 내용은 서버로 전달이 되지 않습니다.<br>서버로 전달하고 싶으면 `<input>`에다가 전부 `name=" "` 속성을 열어서 아무거나 영어로 작명해주면 됩니다. 

- 이제 여기다가 서버에 만들어둔 /url과 method 채우면 되는데 <br>아직 서버기능 개발 안했으니까 <br>아무거나 채워넣고 서버에서 이거 그대로 기능을 만들어두면 되겠군요.

- 저는 URL을 /add로 작명해봤습니다.<br>서버에서 이제 /add 로 POST요청 받는 코드 작성하면 되겠군요. 

### 서버는 글 받으면 잘보냈나 검사해보기 
- 이제 이거 2번기능 구현하면 될 것 같습니다. 
- 그 전에 셋팅이 하나 필요한데<br>유저가 보낸 정보를 서버에서 쉽게 출력해보고 싶으면

```js
app.use(express.json())
app.use(express.urlencoded({extended:true})) 
```

- 서버파일 상단 쯤에 이런거 추가합시다. <br>원래 유저가 데이터를 보내면 그걸 꺼내쓰는 코드가 좀 귀찮게 되어있는데<br>그걸 `요청.body`로 쉽게 꺼내쓸 수 있게 도와주는 코드입니다. 

![](Node.js%20&%20MongoDB%202-2.png)

- 일단 유저가 /add로 POST요청하면서 글을 보내고 있기 때문에<br>누가 POST요청시 뭔가 코드를 실행해주고 싶으면

```js
app.post('/add', (요청, 응답)=>{
  console.log(요청.body)
  실행할코드~
}) 
```

- 이거 써놓고 시작하면 됩니다.<br>누가 /add로 POST요청시 안에있는 코드 실행하라는 뜻입니다. 

- 그리고 중요한게 있는데 여기 안에서 `요청.body`라고 쓰면 유저가 `<input>`으로 보낸 데이터를 출력해볼 수 있습니다. <br>그래서 요청.body 출력 잘 되는지 진짜로 글작성하고 전송버튼 눌러서 POST요청 날려봅시다. 

- 유저가 보낸 글을 DB에 저장하는 3번 기능은 알아서 숙제로 구현해오시면 되겠습니다. 

```ad-todo
오늘의 숙제 : 
유저가 /add로 POST요청하면 작성한 제목과 내용이 서버로 전달되고 있습니다.  
그 제목과 내용을 DB에 저장해봅시다. 
안배운걸 내가 어떻게하냐고요?
안배운건 당연히 'mongodb 데이터 저장하는법' 이런거 검색해봐야지 생각한다고 나오는게 아닙니다. 
```

```js
app.post("/add", (요청, 응답) => {
  db.collection("post").insertOne({
    title: `${요청.body["title"]}`,
    content: `${요청.body["content"]}`,
  });
  console.log("저장완료");
});
```