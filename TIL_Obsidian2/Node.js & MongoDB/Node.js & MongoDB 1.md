---
tags:
  - CodingApple/NodejsMongoDB
---
### 남자라면 서버개발을 할 줄 알아야함
![](assets/Node.js%20&%20MongoDB%201-23.png)
- ▲ 웹서비스를 하나 만들고 싶으면 일단 웹페이지가 필요합니다.<br>이건 html css javascript 쓰면 쉽게 만들 수 있는데<br>근데 이거 프론트엔드 껍데기만으로는 아무것도 할 수 없습니다.
- 👉 실제 동작하는 나만의 서비스를 만들고 싶으면 *서버기능*이 필요합니다.


- 서버 기능이 있어야
	- DB저장기능 
	- 이미지업로드기능
	- 회원기능
	- 채팅기능
	- 검색기능
- 이런 것들을 구현할 수 있으니까요.

- 근데 생각보다 서버개발을 어렵고 복잡한걸로 알고계신 분들이 많은데<br>👉 그건 가르치는 사람이 이상하게 어렵게 가르쳐서 그렇지 실은 별로 어렵지는 않습니다.

### 서버개발자가 짜는 코드
- 서버개발 어떻게 하는 거냐면<br>모든 웹서비스는 요청하면 응답해주는 식으로 이루어져있습니다.

![](assets/Node.js%20&%20MongoDB%201.png)

- 예를 들어서 웹툰을 보고싶으면 어떻게해요? 
- 가만히 있는데 네이버가 갑자기 웹툰을 보내주진 않습니다. 
- 여러분이 네이버 웹툰 들어가서 이거저거 눌러서 네이버웹툰 서버에 웹툰 좀 달라고 요청하죠?
- 그럼 서버가 웹툰을 보내줍니다.

![](assets/Node.js%20&%20MongoDB%201-24.png)

- 유튜브 영상을 보고싶으면 어떻게해요?
- 유튜브 들어가서 이거저거 눌러서 영상 달라고 유튜브 서버에다가 요청합니다. 
- 그럼 유튜브 서버는 영상을 보내줍니다.
- 그게 기본적인 웹서비스의 동작방식입니다.
- _유저가 뭔가 데이터를 달라고 하면 서버는 데이터를 보내는 식으로 동작합니다.__ 

- 👉 그리고 그런 식으로 **누가 데이터요청하면 데이터 보내주는 간단한 프로그램**을 우리가 서버라고 부릅니다. 

```ad-tip
그래서 여러분 네이버 웹툰 서버를 만들고 싶으면 
"누가 A 웹툰 달라고 하면 A 웹툰 보내주기"
이렇게 코드짜면 끝입니다. 

그래서 여러분 유튜브 서버를 만들고 싶으면 
"누가 B 영상 달라고 하면 B 영상 보내주기"
이렇게 코드짜면 끝입니다. 

그래서 서버개발자가 짜는 코드는 
"누가 A 요청하면 A 응답해주셈"
기본적으로 이게 99% 입니다. 
```

- 근데 이거 코드를 짤 때 비슷한 코드들이 많아서 이상한 객체지향 문법도 쓰고<br>아니면 가끔 코드를 새로 만들기 귀찮아서 코드중복을 줄일 수 있는 문법도 쓰고

- 코드가 길어지면 파일도 분리하고<br>예외적인 사항을 처리하는 if문도 길게 짜고 그럴 뿐입니다.

- 문법적 기교 빼면 **핵심은 "누가 A 요청하면 A 응답해주기"** 이거밖에 없습니다.<br>그래서 서버개발 별거 아니니까 같이 만들어봅시다. %%빡대가리라도 크게 상관없음%%

### 만들 프로젝트 
- 강의에선 nodejs express mongodb를 이용해서 서버개발을 좀 해보도록 합시다. 
- 간단한 게시판을 만들어보면서 서버개발을 배워볼건데<br>게시판말고도 더 간지나고 멋있는 프로젝트많은데 왜 게시판 만드냐면
	1. 이 강의 목적은 여러분들 이해시켜서 혼자 코드짤 수 있는 사람만드는거라 최대한 쉽고 간단한 프로젝트를 해야하고 
	2. 어짜피 다른 웹서비스를 만들고 싶어도 웹서비스의 99%는 게시판이랑 기능이 똑같습니다.

![](assets/Node.js%20&%20MongoDB%201-25.png)

![](assets/Node.js%20&%20MongoDB%201-26.png)

#### 필요한 사전지식 
- html css 기초
- 자바스크립트 기초 (var if function for array object)
	- 👉이런 것들이 필요합니다.

- *"내가 var if function for array object 문법을 책보고 한번 슥 따라쳐봤다"* 가 아니라<br>*"내가 코드짜다가 필요할 때 var if function for array object 문법을 꺼내서 직접 사용할 줄 안다"* 가 권장사항인데 <br>솔직히 그 정도까진 기대안하니까 강의하면서 다시 설명하긴 합니다.
- 프로그래밍이 아예 처음이면 html 기초, 자바스크립트 기초강의부터 추천드립니다.


### Nodejs의 장점이 뭐냐면
- 웹서버를 만들고 싶으면 여러 언어와 프레임워크가 있는데<br>이 중에 자바스크립트 기반의 Node.js를 사용하는 사람들이 많습니다. 
- 일단 쉽고 성능도 어느정도 나와서 많이 쓰는 것도 있고 (Bun이나 Fastify 사용시 Rust, Go로 만든 서버와 성능이 삐까뜨는 벤치마크도 많습니다)<br>*non-blocking I/O, 비동기처리가 가능하다는 장점*이 있어서 쓴다고 하는데 그게 대체 무슨 뜻인지 알아봅시다.


#### Node.js가 뭐냐면
- 자바스크립트라는 언어가 있습니다.<br>실은 서버만들고 그런 용도는 아니고 <br>html 웹페이지에 여러가지 기능을 넣기 위해 만들어진 언어입니다.<br>그래서 비유하자면 html 따까리 언어가 자바스크립트임

- 근데 자바스크립트를 짜놨으면 이걸 누가 실행해줘야하지않겠습니까<br>실은 여러분들이 짠 자바스크립트는 누가 실행하냐면 웹브라우저가 책임지고 실행해줍니다.

- 크롬브라우저안에도 자바스크립트 실행엔진이 있습니다. <br>구글이 V8이라고 이름을 지어놨는데<br>이걸 하도 성능좋게 잘 만들어서<br>이걸 자랑삼아서 똑 떼어서 *독립적인 실행파일로 출시했는데 이걸 Node.js*라고 부릅니다. 

- 그래서 Node.js는 자바스크립트 파일 실행기일 뿐입니다. <br>👉 이거 설치하면 컴퓨터 아무데서나 자바스크립트로 작성한 파일을 실행할 수 있습니다. (멋있는 말로 Node.js를 자바스크립트 런타임이라고 부름)

- 그래서 Node.js만 쓰면 코드에디터, 윈도우 프로그램 이런 온갖 프로그램을 만들 수 있다보니까<br>사람들이 Nodejs로 웹서버도 만들기 시작한 겁니다. 

- 그런데 특유의 간결한 문법과 성능 덕분에 인기가 아직 많습니다.<br>그리고 웹개발할 때 프론트엔드에서 자바스크립트를 꼭 사용하기 때문에<br>프론트엔드 할 줄 알면 Node.js로 백엔드 서버개발도 매우 쉽게 배울 수 있다는 것도 장점입니다. <br>👉 언어 하나로 프론트엔드랑 백엔드 전부 작성가능

#### Non-blocking I/O
- 왜 성능이 좋은지 잠깐 짚고 넘어가봅시다. <br>Node.js는 non-blocking 이라는 장점 덕분에 보다 빠릿빠릿한 웹서버를 만들 수 있는데<br>예를 들어 지금부터 영화예매 서비스를 하나 만든다고 합시다.

- 어떻게 코드짜냐면 
	1. 누가 영화예매 요청을 하면
	2. 영화를 예매해서 결과를 유저에게 보내주는 프로그램을 하나 만들기<br>끝입니다. 

- 근데 Node.js 말고 파이썬 자바스프링 같은거 대충 써서 일반방식으로 서버를 만들어놓으면 어떤 일이 일어나냐면 <br>기본적으로 **먼저 온 순서대로 차례차례 예매 요청을 처리해줍니다.**

- 거의 모든 프로그래밍 언어는 차례로 한 줄 한 줄 실행되기 때문에<br>영화예매 서비스를 만들어도 기본적으로 그렇게 동작합니다.

##### 일반적인 서버의 경우
![](assets/Node.js%20&%20MongoDB%201-27.png)

- 근데 이렇게 하면 문제가 있습니다. <br>예를 들어 영화표 발급해주는데 1초 걸리는데<br>200장을 예매하는 미친놈이 있으면 어떻게 되죠? <br>이놈 처리하는데 200초가 소요되겠군요.

- 근데 이러면 뒤에 있던 고객도 200초를 대기해야하는 불상사가 일어납니다.  <br>👉 그래서 서버 대충만들면 중간중간 어려운 요청이 들어오면 서버 기능이 전체적으로 느려질 수 있습니다. 

##### Node.js의 경우 (Non-blocking I/O)
![](assets/Node.js%20&%20MongoDB%201-28.png)

- 근데 Node.js를 사용해서 서버를 만들어놓은 경우 어떤 식으로 처리를 해주냐면 
	1. 우선 유저들이 들어오면 요청부터 전부 받습니다 
	2. 그 다음에 빨리빨리 처리가 완료되는 순서대로 유저에게 결과를 보내줍니다.
- 👉 그래서 늦게온 유저도 1장만 예매한다면 빨리빨리 결과를 받아볼 수 있는 겁니다. 200개 예매하던 미친놈은 똑같이 200초 후에 받아보면 되는거고요. 

- 이런식으로 요청들을 처리해주는걸 멋진말로 non-blocking, 비동기 처리라고 합니다. <br>중간에 시간이 오래걸리는 작업을 만나면 그걸 잠깐 제껴두고 다른거부터 우선 처리한다는 소리입니다.

- 물론 정확히 말하면 Node.js 안에서 비동기처리를 지원하는 코드를 작성해야 이런 식으로 효율적인 처리를 매우 쉽게 구현할 수 있는건데<br>대부분의 코드가 비동기처리를 지원하는 코드기 때문에 그냥 기본으로 저렇게 동작하는구나라고 생각해도 됩니다. 

- 👉참고로 파일입출력, DB입출력 이런거 전부 비동기처리가 매우 쉽습니다.


#### 서버 확장하면 되는거 아님?
- 물론 고객이 많으면
	1. 창구 갯수 (thread)를 늘리거나
	2. 창구 처리속도를 늘리거나 (CPU를 업그레이드) 하는 식으로도 대응가능합니다.
- 👉 근데 thread를 늘리면 그만큼 단점도 존재합니다. 

- 많은 창구에서 데이터를 동시에 가져다쓰고 수정하고 삭제하고 그러면<br>데이터의 정확도가 떨어지고, <br>정확도 떨어지는걸 막기 위해 락을 걸면 또 그만큼 처리속도가 늦어지고 <br>그런 문제가 발생하기 때문에 비동기식 처리를 하려고 온갖 노력을 하는 웹서버들이 많은데<br>Node.js 쓰면 기본이 비동기처리임

#### Node.js 단점
- CPU를 많이 갈궈야하는
	- 이미지변환
	- 동영상압축
	- 숫자계산
- 이런 작업이 많이 들어가야하면 관련 라이브러리같은것도 적고 싱글스레드라 성능도 좋지 않을 수 있어서 <br>그런 기능이 필요하면 Node.js는 별로일 수 있습니다. 

- 👉그래서 _비교적 가벼운 요청을 많이 처리해야하는 SNS, 게시판 같은거 만들 때 좋다는 인식_ 이 있습니다. 

- 자바스크립트에 원래 타입시스템이 없어서<br>타입관련 버그들 많다고 싫어하는 사람들도 있었는데<br>*지금은 타입스크립트 쓸 수 있어*서 별걱정 안해도 됩니다. 


### Node.js, Express 설치와 셋팅

#### 개발환경 셋팅
- 개발환경 셋팅부터 해보도록 합시다. <br>요즘은 맥북이나 윈도우나 별 차이없음 

1. nodejs 구글에 검색하면 맨처음에 뜨는 사이트가 있을텐데<br>거기서 LTS 버전 다운받아서 설치까지 합시다. 
	- 설치할 때 경로같은건 안만지는게 좋을 수도 있습니다. 
	- 윈도우는 chocolatey 같은거 설치안해도 됩니다. 

2. 에디터가 하나 필요한데 VSCode 에디터 구글에 검색해서 설치합시다. 

#### 프로젝트 생성은 
1. 코드짤 작업용 폴더를 하나 만들고<br>VSCode 에디터 켜서 상단 `file - open folder` 눌러서 에디터로 작업용 폴더를 오픈합시다.

2. server.js 파일을 하나 만들어줍시다. <br>거기다가 서버코드짤 것임 

3. 에디터 상단 terminal 눌러서 터미널을 열 수 있는데<br>거기다가 `npm init -y` 를 입력합시다. <br>package.json 파일 생성해주는 명령어입니다. 

4. 터미널에 `npm install express`를 입력합시다. <br>express라는 라이브러리를 설치하는 명령어입니다. 
	- 처음부터 쌩으로 코드짜면 너무 힘들기 때문에<br>사람들 많이 쓰는 express라는 라이브러리를 써서 서버를 만들 것임 

5. server.js 파일안에 서버코드 작성

```js
const express = require('express')
const app = express()

app.listen(8080, () => {
    console.log('http://localhost:8080 에서 서버 실행중')
})

app.get('/', (요청, 응답) => {
  응답.send('반갑다')
}) 
```

![](assets/Node.js%20&%20MongoDB%201-29.png)

- 이제 express 라이브러리를 이용해서 쉽게 서버를 만들어볼 수 있습니다.
- 대충 설명하자면
	- 맨 위의 2줄은 설치한 라이브러리 불러오는 코드고 
	- app.listen() 부분이 실제 서버 띄우라는 뜻입니다. 8080포트에 띄우라고 코드짰습니다. 
	- app.get() 부분은 누군가 내 사이트 메인페이지 접속하면 '반갑다'라는 글자를 보내라는 뜻입니다.

6. 코드짠걸 실행해봅시다. <br>실행해야 뭐가 동작하지 않겠습니까<br>터미널 열어서 `node server.js` 입력하면 server.js 파일이 실행되고<br>방금 만든 서버코드도 실행됩니다. 

- 진짠지 확인하고 싶으면 브라우저 열어서 http://localhost:8080으로 접속해봅시다.


#### PORT가 뭐냐면 
- 여러분 컴퓨터는 항상 외부 컴퓨터와 통신할 수 있게 설계되어있습니다.<br>랜선만 꽂혀있으면 다른 사람이 여러분 컴퓨터로 접속을 할 수 있고 그렇습니다. <br>웹서버도 실은 다른 사람 컴퓨터에 접속하는 행위랑 똑같습니다. 접속하면 웹페이지를 보여주는 것일 뿐

- 하지만 평상시엔 남들이 내 컴퓨터에 무단으로 접속을 할 수는 없습니다. <br>여러분들이 컴퓨터에 구멍을 하나 뚫어놓아야 거기로 외부 사람들이 내 컴퓨터로 접속할 수 있습니다<br>구멍을 전문용어로 PORT라고 부르고 컴퓨터에는 내 맘대로 오픈할 수 있는 포트 구멍이 6만개 정도 있습니다.

- 그래서 아까 누가 내 컴퓨터에 접속할 수 있게 만들기 위해서 <br>8080번째 포트하나를 맘대로 연겁니다. <br>이제 외부 컴퓨터가 여러분 아이피주소:8080이라고 브라우저 주소창에 입력하면<br>여러분 컴퓨터로 들어올 수 있게 되는 것입니다. <br>(터미널에 ipconfig 치면 뜨는 그 아이피주소임)

- 참고로 열 수 있는 포트는 6만개 정도 있는데<br>컴퓨터가 이미 예약해서 쓰고 있는 포트번호들도 여러개 있습니다.<br>그런건 쓰면 안됩니다.

#### 터미널에서 npm으로 하는게 뭔가 안되면
**1. npm : command not found 에러** 
- command not found 라는 에러가 터미널에 뜨면 <br>nodejs 설치가 아직 안되었거나 제대로 안된 것입니다. <br>nodejs 삭제했다가 공식 홈페이지에서 LTS버전 제대로 다운받아서 설치합시다.<br>맥도 brew 어쩌구 그런걸로 설치하지 마시고 다운받읍시다.

**2. 맥북에서 권한, permission이 없다 어쩌구 에러**
```shell
npm ERR! syscall access
npm ERR! Error: EACCES: permission denied, access '/usr/local/lib/node_modules'
```
- 폴더 수정 권한이 없다고 에러를 띄우는 것입니다.<br>위의 에러는 /usr/local/lib/node_modules 라는 폴더에 수정권한을 주면 됩니다.

```shell
sudo chown -R $USER 위에 에러 뜬 경로
```
- 터미널에 이거 입력해봅시다.

```shell
sudo npm install express
```
- 그래도 안되면 npm으로 뭔가 할 때 그냥 sudo라는 단어를 앞에 붙여서 실행합시다.<br>맥북 비번 입력하라고 하면 입력합시다.

**3. 윈도우 Powershell에서 빨간글씨로 허가되지않은 스크립트, 보안오류가 뜸**
- 시작 - 검색 - Powershell 검색 - 우클릭 - 관리자 권한으로 실행한 뒤<br>Set-ExecutionPolicy Unrestricted 라고 입력해보고<br>에디터 껐다 켭시다.

**4. 윈도우도 npm으로 뭐 할때 권한이 없다 어쩌구 에러**  
- 그럼 powershell을 관리자 권한으로 열어서 실행하면 됩니다.

![](assets/Node.js%20&%20MongoDB%201-30.png)

- ▲ 직접 작업폴더로 들어가서 상단에서 파일 - PowerShell 열기 - 관리자권한으로 PowerShell 열기 눌러서 터미널을 엽니다.<br>이렇게 연 다음에 npm install 어쩌구가 되면 앞으로 터미널에서 뭐 하라고 하면 터미널 이렇게 켜서 사용합시다. 

- 이거 말고도 다른 에러가 있을 수 있어서 <br>에러메세지는 직접 구글 검색해보는게 빠릅니다.


### 웹페이지 보내주려면 (라우팅)
- 저번시간에 서버를 간단하게 만들어봤습니다.<br>근데 메인페이지 하나만 만들어봤는데<br>이번엔 여러 페이지를 더 만들고 싶으면 어떻게할지 알아봅시다. 

- 근데 만들기 전에 실제 사이트들은 어떤 식으로 여러가지 페이지들을 만들어놨는지 구경부터 해봅시다. <br>예를 들어 네이버 웹툰같은 사이트 방문해보면 <br>**comic.naver.com**<br>여기로 접속하면 메인페이지가 보이긴 하는데

- URL 뒤에다가 /webtoon 을 붙여서 접속하면 오늘의 웹툰 페이지 보여주고<br>URL 뒤에다가 /challenge 를 붙여서 접속하면 도전만화 페이지를 보여줍니다. 

- 네이버 웹툰 말고도 다른 사이트도 이런 방식으로 페이지를 나눠놓는데<br>우리도 그렇게 만들면 될 것 같습니다. <br>주소창에 입력하는 URL을 기반으로 각각 다른 페이지를 보내줍시다.

#### 새로운 페이지를 만들어보자 
- 오늘의 뉴스같은걸 보여주는 페이지를 만들고싶으면 어쩌죠? <br>예를 들면 /news라는 URL로 유저가 접속하면 오늘 뉴스를 보내주는 페이지를 하나 만들고 싶습니다. <br>그럼 코드를 어떻게 짜야될까요?<br>저번시간코드를 잘 살펴보면 되어서 눈치만 좋으면 실은 알아서 할 수 있습니다.

```js
app.get('/어쩌구', (요청, 응답)=>{
  응답.send('보내줄 웹페이지 내용')
}) 
```

- 새로운 페이지를 하나 만들고 싶으면 express문법으로 이렇게 작성하면 됩니다.<br>`/어쩌구` 부분은 자유롭게 작명하고 보내줄 내용 부분도 알아서 작성하면 끝입니다.

![](assets/Node.js%20&%20MongoDB%201-31.png)

```js
app.get('/news', (요청, 응답)=>{
  응답.send('오늘 비옴')
}) 
```

- 아까 /news로 접속하면 뉴스같은거 보내주는 페이지 만들고 싶다고 했으니 저는 이렇게 작성해봤습니다. <br>그럼 이제 파일저장하고 터미널에서 실행하고 있던거 `컨트롤 + c` 눌러서 끄고 <br>다시 node server.js 이거 파일 실행해보면 반영됩니다.<br>진짜로 웹브라우저 켜서 /news 페이지로 접속해보시길 바랍니다. %%새로운페이지 완성%%

**Q. 그럼 유저가 /shop 으로 접속하면 '쇼핑페이지입니다~' 라는 글자를 보여주고 싶으면 코드 어떻게 짬?**

```js
app.get("/shop", function (요청, 응답) {
  응답.send("쇼핑페이지입니다~");
});
```

```ad-tip
_(참고) 이런거 새로나오는 문법 하나하나 외우고 이해하려고 하는 분들이 있는데 그러지 마십시오._ 
그냥 express 만든사람이 이렇게 쓰라고 만들어놓은 'express 라이브러리 사용법'이기 때문에
우리도 거기 맞춰서 쓰는 것일 뿐이지 문법을 굳이 이해할 필요는 없습니다 
그리고 까먹으면 express 사용법 검색해보면 되기 때문에 그냥 복붙해서 써도 별 상관없습니다. 

그래서 서버개발은 뭔가 이해하고 직접 코드짜는 일이 별로 없고
그냥 라이브러리 사용법대로 코드짜면 개발 끝입니다.

오늘의 결론은 그냥 여러분들 사이트에 새로운 페이지가 하나 필요할 때 마다 요 템플릿 그대로 복붙해서 쓰면 됩니다. 
```

#### 잠깐 자바스크립트 문법 설명 
```js
function 함수1(){ }
var 함수2 = () => { }
```
- 자바스크립트에선 `function 키워드`를 쓰거나<br>그거대신 **=> 기호**를 쓰거나 해서 함수를 만들 수 있습니다.

```js
app.get('/news', (요청, 응답) => {
  응답.send('오늘 비옴')
}) 
```

- 그래서 여기 있던 `() => {}` 부분도 함수 만들어서 집어넣는 문법입니다.<br>근데 지금보면 함수안에 함수를 집어넣고 있죠? <br>(`app.get()` 도 실은 함수입니다 함수 사용문법임)

- 이런 식으로 다른 함수 소괄호 안에 들어가는 함수를 멋있는 말로 **콜백함수**라고 부릅니다. <br>그냥 이름이 멋있으니까 알아두시면 됩니다.  <br>실은 자바스크립트에서 _특정 함수들이나 특정 코드들을 순차적으로 차례차례 실행하고 싶을 때_ 콜백함수를 자주 사용합니다.

```js
app.get('/news', (요청, 응답) => {
  응답.send('오늘 비옴')
}) 
```

- 그래서 이 코드가 어떻게 실행되냐면 <br>누가 `/news`로 접속하면 자동으로 `app.get()` 이라는게 함수가 실행되어서 접속요청을 처리해주는데<br>근데 app.get 함수가 실행되고 나서 그 다음에 바로 콜백함수 내에 있는 코드가 실행됩니다.<br>그런 식으로 동작합니다. 

- 참고로 콜백함수는 맘대로 쓸 수는 없고 콜백함수 쓰라는 곳만 쓸 수 있습니다. <br>그래서 아무튼 함수 소괄호 안에 들어가는 함수를 **'콜백함수'** 라고 부른다는 것만 상식으로 알아둡시다.


#### html 파일 보내기 
- 지금은 메인페이지 접속하면 단순한 문자하나만 보내고 있는데<br>그게 싫고 이쁜 웹페이지를 보여주고싶다면 html 파일을 보내주면 됩니다.

- html 파일이 뭐냐면 그냥 웹페이지 레이아웃 만들 때 쓰는 파일입니다. <br>그 안에 html css 문법으로 코드 열심히 짜면 이쁜 웹페이지 레이아웃을 만들 수 있습니다.

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  안뇽
</body>
</html> 
```

- server.js 파일 옆에 index.html 같은 html 파일 하나만 만들고 위처럼 내용을 채워봅시다.<br>이게 html 파일 기본 템플릿이고 `<body>` 안에 웹페이지 디자인 시작하면 됩니다. 
- 기본 템플릿은 매번 타이핑할 필요 없고 VSCode 에디터에선 `! 느낌표` 적고 엔터나 탭키 누르면 자동완성 될 수 있습니다. 
- 아무튼 만든 html 파일을 유저에게 전송하려면 어떻게 하냐면

```js
app.get('/', function(요청, 응답) {
  응답.sendFile(__dirname + '/index.html')
})
```

- 누가 메인페이지 방문시 html 파일 보내라고 코드는 이렇게 짭니다. 
1. 응답.send가 아니라 .sendFile('파일경로') 입력하면 이 파일을 유저에게 보내줍니다. 
2. 파일경로를 적고 싶으면 
	- `__dirname`이라고 쓰면 (언더바 2개) 현재 server.js 파일의 절대경로가 나옵니다.
	- 근데 index.html은 server.js와 같은 폴더에 있으니까 `__dirname` 뒤에 `/index.html` 만 추가하면 index.html 파일경로가 나올거같군요.

- 그래서 터미널에서 실행하고있던거 끄고 다시 터미널에 node server.js 입력해서 파일실행해봅시다.
- 이제 메인페이지로 접속하면 html 파일이 보이죠?
	- %%안보이면 오타거나 파일 저장을 안한 것임 %%

```ad-note
오늘 배운 내용을 요약해보면
1. 웹페이지 하나 만들고 싶으면 app.get 부터 3줄 가져다가 씁시다.
2. 함수 소괄호 안에 들어가는 함수를 콜백함수라고 부르고 코드들을 순차적으로 실행할 때 가끔 씁니다.  
3. html파일 보내고 싶으면 `응답.sendFile()` 쓰면 됩니다.
```

```ad-todo
오늘의 숙제 :
누가 `/about`으로 접속하면 여러분이 누군지 대충 소개하는 html 파일을 보내줍시다.
그럼 html 파일도 하나 더 필요하겠죠?
쉬워서 답은 없음 
```

```js
app.get("/about", function (요청, 응답) {
  응답.sendFile(__dirname + "/about.html");
});
```

```html
<!-- about.html --> 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello, This is Ramy Jo page</h1>
  </body>
</html>

```


### 웹페이지에 디자인 넣으려면
- 이쯤되면 귀찮은 점이 하나 있을텐데  <br>소스코드를 수정했을 경우 `ctrl + c` 눌러서 터미널에 실행하던걸 끄고 <br>다시 `node server.js`를 입력해야 수정사항을 미리볼 수 있습니다. <br>매번 입력하는게 귀찮으면 `nodemon` 사용하면 됩니다. 

- 터미널 열어서 실행되고있던거 `ctrl + c` 눌러서 끄고

```shell
npm install -g nodemon

nodemon server.js
```

- 그럼 이제 서버파일을 띄울 때 node말고 nodemon server.js 이렇게 입력해둘 수 있는데<br>그러면 소스코드를 변경 후 파일저장하면 얘가 알아서 서버도 재시작해줍니다. <br>이제 코드짜고 저장만 하면 끝임

#### static파일 (css파일) 첨부하기
- html에 디자인을 넣고 싶으면 css 파일에 작성하는게 일반적인데 <br>css 파일 하나 만들고 디자인 열심히 한 다음에 html 파일에 넣어서 쓰면 됩니다. 
![](assets/Node.js%20&%20MongoDB%201-32.png)

- ▲ css 파일처럼 쓸데없는 파일이나 이미지는 public 폴더같은 곳에 넣어두는게 일반적입니다. 
- 이제 html 파일에서 css 파일을 가져다가 쓰고 싶으면 `<link> 태그` 추가하면 되는데 <br>근데 여기까지만 하면 아마 css 반영이 안될걸요 <br>왜냐면 css, 이미지, js 파일들을 html 안에서 사용하고 싶으면<br>우선 그게 들어있는 폴더를 **서버에 등록**부터 해놔야합니다.

```js
app.use(express.static(__dirname + '/public'));
```

- public폴더안에 있는 파일들을 html에서 가져다가 쓰고 싶으면 <br>서버파일에 app.use라는 문법으로 public 폴더를 등록해놔야합니다. 
- 그럼 이제 public 폴더안에 있는 css파일 이미지파일 js파일은 전부 html에서 가져다가 쓸 수 있습니다. 
- 참고로 css, js, 이미지 파일들을 static 파일들이라고 부릅니다. 

```html
<link href="/main.css" rel="stylesheet">
```
- 그럼 이제 html 파일에서 css 파일을 첨부해서 사용할 수 있습니다.

#### 상단메뉴 만들기 
```html
<div class="nav">
    <a class="logo">AppleForum</a>
    <a>Page1</a>
    <a>Page2</a>
</div> 
```

```css
body {
  margin: 0;
}
.nav {
  display: flex;
  padding: 15px;
  align-items: center;
  background : white;
}
.nav a {
  margin-right: 10px;
}
.logo {
  font-weight: bold;
}
```

#### Bootstrap
- 혼자서 웹개발하는 분들에게 유용한거 하나 소개하자면 <br>내가 css 디자인 실력이 없으면 html css 레이아웃짜라고 하면 손발이 벌벌 떨릴텐데  <br>좀 쉽게 웹페이지 디자인을 하고 싶으면 css 라이브러리 설치해서 사용해도 됩니다.<br>가장 유명한게 Bootstrap입니다.
![](assets/Node.js%20&%20MongoDB%201-33.png)

- https://getbootstrap.com/

- 대충 설치법은<br>사이트 들어가면 docs 버튼같은게 있는데 누르면 설치방법같은게 나옵니다. 
	1. 거기서 bootstrap.css 파일을 찾아서 html파일의 `<head>` 태그 안에 첨부하고 
	2. bootstrap.js 파일을 찾아서 html파일의 `<body>`태그 끝나기 전에 첨부하면 설치 끝입니다. 
- 그럼 이 html 파일에서 복붙식으로 UI 개발이 가능합니다

##### Bootstrap CDN
```html
<!-- bootstrap.css -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
```

```html
<!-- bootstrap.js -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
```


```ad-tip
Q. 저는 색이 마음에 안드는데요?
- 당연히 디자인을 그대로 써야하는게 아니라 
수정하려면 여러분만의 클래스명 만들어서 붙이면 끝입니다.
처음부터 모든걸 쌩으로 만드는 것 보다
이렇게 기본 스타일에서 수정해서 쓰는게 더 빠르고 쉽습니다.
다만 bootstrap의 css 파일, js 파일 용량이 커서 이런건 손해일 수 있습니다. 
```


### MongoDB 호스팅받고 셋팅하기
- 게시판을 만든다고 했는데 게시판을 만들려면 유저들이 작성한 게시물들을 영구적으로 보관할 곳이 하나 필요하지 않겠습니까<br>뭐 대충하고 싶으면 엑셀이나 메모장열어서 거기다가 유저들의 게시물들을 적어놔도 되는데 <br>보통은 그런거 말고 실제 서비스들은 데이터베이스에 데이터들을 저장해놓습니다.<br>데이터베이스가 훨씬 입출력이 빠르고 대용량의 데이터를 보관할 수 있으니까요.
#### MongoDB 사이트 가입, 계정 생성 간 특이사항
- 무료 티어 선택
- DB 접속용 아이디/비번 생성(**꼭 적어두기**)
- 역할을 `atlas admin`으로 설정
	- 👉 그래야 해당 아이디로 node.js 에서 제한 없이 활용 가능
- Network Access 메뉴에서 IP를 추가
	- Allow access from anywhere을 누르시거나 0.0.0.0/0 을 추가

#### 데이터베이스 종류 
- 그래서 여러가지 데이터베이스들 중에 하나 고르면 되는데<br>데이터베이스는 크게 두가지 종류가 있는데<br>관계형 & 비관계형 데이터베이스가 있습니다

![](assets/Node.js%20&%20MongoDB%201-34.png)

- 관계형 데이터베이스들은 그냥 엑셀이랑 똑같습니다. <br>표가 하나 있고 거기다가 데이터를 한줄한줄 차례로 보관하면 됩니다.<br>관계형 데이터베이스를 쓰고 싶으면 DBMS를 설치하면 되는데 <br>MySQL, PostgreSQL, Oracle, SQLite, MSSQL<br>이런거 중에 하나 골라서 사용하면 됩니다.<br>한국에선 MySQL, PostgreSQL, Oracle 점유율이 높습니다.

- 근데 관계형 데이터베이스를 쓰면 <br>데이터를 입출력할 때 SQL이라는 언어를 사용해서 입출력해야하는게 좀 귀찮은 점이고 데이터를 저장할 때 그냥저장하는게 아니라 **정규화**라는걸 해서 저장합니다.

![](assets/Node.js%20&%20MongoDB%201-35.png)

- ▲ 손흥민이라는 데이터는 부분은 현재 테이블과 관련없으니<br>다른 테이블로 쪼개고 있습니다. 
- 현재 테이블의 주제와 맞지 않는 것들을 다른 테이블로 분리하는 작업을 있어보이는 말로 **정규화**라고 합니다.<br>그리고 그걸 해놔야 나중에 데이터가 정확도가 높아집니다. 
- 그래서 데이터의 정확도가 중요한 서비스를 만들고 싶으면 <br>일반적으로 관계형 데이터베이스를 많이 선택합니다. 


- 비관계형 데이터베이스는 <br>좀 더 자유로운 형식으로 데이터를 저장할 수 있게 만든 데이터베이스인데<br>예를 들어 Redis는 `{ 데이터이름 : 데이터값 }` 형식으로 데이터를 저장할 수 있고 <br>MongoDB도 그거랑 유사하게 데이터를 저장할 수 있습니다.

![](assets/Node.js%20&%20MongoDB%201-36.png)

- 그리고 테이블 쪼개기인 정규화를 안하고 저장하는게 권장사항이라서<br>데이터를 입출력할 때 생각할게 없어서 굉장히 빨리 할 수 있습니다.
- 근데 그 대신 데이터의 정확도가 떨어지고<br>정규화를 안해놨다면 나중에 이름같은거 하나를 수정삭제하고 싶으면 수많은 부분을 수정해야하기 때문에 그런 것들이 귀찮을 수 있습니다. 
- 그래서 데이터 입출력이 빨라야하는데 정확도가 좋지는 않아도 되는<br>게시판이나 SNS를 만들 때는 이런거 쓰는게 나을 수 있습니다.

- 근데 항상 정확도가 중요하면 관계형,<br>입출력빠른게 중요하면 비관계형<br>이렇게 나눌 수 없는게<br>여러분이 데이터베이스를 어떻게 쓰냐에 따라서 다를 수도 있어서<br>그냥 경향만 그렇구나라고 아시면 될거같습니다.  <br>MongoDB도 정규화를 하면서 정확도높게 쓸 수 있습니다.<br>%%근데 살짝 비효율적일 뿐임%% 

![](assets/Node.js%20&%20MongoDB%201-37.png)

![](assets/Node.js%20&%20MongoDB%201-38.png)

- 그래서 우리는 이 중에 MongoDB를 사용해보도록 할건데  <br>왜냐면 SQL같은 언어를 배울 필요도 없고 정규화, 테이블스키마생성 그런걸 안해도 되어서 매우 쓰기 쉽습니다. 

- 그리고 MongoDB는 document 데이터베이스라고 부르기도 하는데<br>왜냐면 데이터를 어떤 식으로 저장하냐면<br>우선 collection을 만들고 그안에 document를 만들어서 거기 데이터를 기록해놓습니다.

![](assets/Node.js%20&%20MongoDB%201-39.png)

![](assets/Node.js%20&%20MongoDB%201-40.png)
- ▲ 예를 들면 유저들의 이름과 나이를 저장하고 싶으면 이렇게 저장합니다.<br>비유를 하자면 collection은 폴더, document는 파일하나라고 생각하면 되겠습니다. 
- 관계형 데이터베이스로 비유하면 collection은 테이블, document는 하나의 행임 <br>근데 document에다가 데이터를 기록해놓는데<br>실은 자바스크립트 object자료랑 똑같은 모습으로 기록합니다. 
- 그래서 자바스크립트 코드짜던거 그대로 데이터베이스에 밀어넣을 수 있어서 매우 저장과 출력이 편리합니다.

#### MongoDB 호스팅받기
-  MongoDB를 사용해볼건데 사용하고 싶으면 방법이 2개 정도 있습니다.<br>여러분 컴퓨터에 직접 mongodb를 설치해서 쓰거나<br>아니면 클라우드에서 호스팅받아서 쓰거나 <br>둘 중에 하나 선택하면 됩니다.

- 근데 보통 초보자들은 호스팅받아서 쓰는게 좋기 때문에 호스팅을 받도록 합시다.
	1. 가입만하면 무료용량도 제공해주고
	2. 돈내서 업그레이드하면 백업도 자동으로 해주고
	3. replica set이라고 해서 자동으로 3개의 데이터베이스에 분산저장해줘서 하나가 다운되면 자동으로 나머지 2개가 돌아가고
	4. full text search index도 만들 수 있고 (호스팅받아야만 사용가능)
- 안 쓸 이유가 없습니다. 
- mongodb.com 사이트 들어가서 가입하면 무료 호스팅같은걸 받을 수 있으니까 가입하고 호스팅까지 받아옵시다. 

#### Database / collection 만들기
- 셋팅은 완료해놨겠죠<br>요약하자면 무료티어 선택하면되고<br>그 다음에 DB접속용 아이디/비번 만들고 <br>DB접속가능한 아이피주소도 설정해놓으면 끝입니다. 

- 셋팅이 완료되면 collection 아니면 create 버튼이 어딘가에 있을텐데 눌러서 데이터베이스를 하나 만들어봅시다.

![](assets/Node.js%20&%20MongoDB%201-41.png)

- database는 하나의 프로젝트같은 것이고 이름은 맘대로 작명하면 되는데<br>저는 게시판을 만들어볼 것이니 **forum**이라고 할겁니다.  <br>그 안에 collection도 하나 만들라고 하는데 저는 **post**라고 이름지어보겠습니다. <br>그럼 이제 요런 post라는 컬렉션 안에 맘대로 document들을 발행해서 데이터를 저장할 수 있습니다.<br>다음 시간엔 데이터 몇개 저장해놓고 그걸 원할 때 출력해서 보여주는 법을 알아봅시다.


### MongoDB와 서버 연결하려면
- DB에 글을 저장할 준비가 다 된 것 같은데 <br>DB에 데이터 입출력은 누가합니까?<br>유저가 직접 글을 DB에 집어넣고 그러면 편할거같은데 <br>그렇게 해버리면 3일 후에 금방 서비스 종료하는 것입니다.

- 유저에게 다이렉트로 DB 입출력 권한을 주면<br>유저가 DB에 이상한 짓을 하면 큰일나기 때문에<br>중간에 검열하는 친구가 하나 필요합니다.

![](assets/Node.js%20&%20MongoDB%201-42.png)

- 중간에서 이거저거 검사하는 역할은 서버가 담당합니다. <br>예를 들어 글을 하나 DB에 저장하고 싶으면 
	1. 유저가 서버로 게시물을 보내고 
	2. 서버는 그걸 검열해본 후 DB에 저장시켜주면 됩니다.
- 오늘은 서버가 DB와 통신하는 법을 좀 알아보도록 합시다.

#### 서버와 MongoDB 연결
- 서버 프로젝트에서 mongodb를 연결하고 싶으면 <br>일단 mongodb 라이브러리를 설치합시다.
```shell
npm install mongodb@5
```

```js
const { MongoClient } = require('mongodb')

let db
const url = 'mongodb사이트에 있던 님들의 DB 접속 URL'
new MongoClient(url).connect().then((client)=>{
  console.log('DB연결성공')
  db = client.db('forum')
}).catch((err)=>{
  console.log(err)
})
```

- 그리고 이런 코드를 서버파일 상단쯤에 추가합니다. <br>그러면 mongodb 라이브러리 셋팅 끝 <br>간단히 설명하면 님들이 호스팅받은 mongodb에 접속하고 접속 결과를 db라는 변수에 저장했을 뿐입니다.<br>mongodb 라이브러리 사용법이라 굳이 이해할 필요 없습니다.

![](assets/Node.js%20&%20MongoDB%201-47.png)
- ▲ DB접속 URL은 어딨냐면 mongodb 사이트가서 connect 버튼이 어딘가 있을텐데 눌러서 Driver를 선택해봅시다.

```js
mongodb+srv://DB접속아이디:DB접속비번@cluster0.jea.mongodb.net/?retryWrites=true&w=majority 
```

- 그러면 대충 이렇게 생긴게 나오는데 이게 DB접속용 URL입니다.<br>근데 DB접속용 아이디 / 비번자리에 여러분이 만든 **DB접속용 아이디 / 비번**을 잘 집어넣읍시다.<br>mongodb.com 로그인할 때 쓰는 아이디 비번 아님

##### DB접속 URL 관련 참고
![](assets/Node.js%20&%20MongoDB%201-43.png)

![](assets/Node.js%20&%20MongoDB%201-44.png)

![](assets/Node.js%20&%20MongoDB%201-45.png)


![](assets/Node.js%20&%20MongoDB%201-46.png)

```js
const { MongoClient } = require('mongodb')

let db
const url = 'mongodb사이트에 있던 님들의 접속 URL'
new MongoClient(url).connect().then((client)=>{
  console.log('DB연결성공')
  db = client.db('forum')

  app.listen(8080, () => {
    console.log('http://localhost:8080 에서 서버 실행중')
  })

}).catch((err)=>{
  console.log(err)
})
```

- 그리고 app.listen() 이런 코드도 여기 안으로 옮기는게 좀 더 안정적일 수 있습니다. <br>DB접속이 완료 되어야 서버를 띄우는게 좋아보여서요. 

- 진짜 잘 되는지 테스트해보고 싶으면<br>아무 app.get 안에서 db에 데이터저장하는 코드 하나만 써보도록 합시다.<br>그리고 그 `/url`로 접속해서 진짜 DB에 뭔가 저장되나 확인해봅시다.

```js
app.get('/news', ()=>{
  db.collection('post').insertOne({title : '어쩌구'})
})
```

- 대충 이렇게 코드 짜고 `/news` 페이지로 접속하면 진짜로 DB에 뭔가 저장되어있을걸요<br>근데 하지마십쇼 DB들어가서 임시데이터들 지우기 귀찮음<br>다음시간엔 DB데이터 출력해서 보여주는 법을 알아보도록 합시다.


### MongoDB에서 데이터 출력하기 (array/object 문법)
- DB에 게시물 한 두개만 저장해보도록 합시다.
	- mongodb.com 사이트 들어가서
	- collection 버튼 누르면
- 현재 DB에 저장된 데이터들을 구경해볼 수 있는데<br>저번시간에 forum이라는 데이터베이스안에 post 라는 컬렉션 (폴더)를 만들어봤습니다. 

- 이제 심심하니까 여기다가 데이터 몇개만 저장해볼건데 <br>게시판을 만든다고 했으니까 유저 게시물을 post 컬렉션에 임시로 몇개 만들어봅시다. <br>insert document 버튼이 어딘가 있을텐데 누르면 데이터를 저장할 수 있습니다.

```js
title : '어쩌구'
content : '저쩌구'
```

- 이런 형식으로 대충 유저 게시물을 두어개 정도 저장해보도록 합시다. <br>document에는 **데이터이름 : 데이터값** 형식으로 데이터를 저장할 수 있습니다. <br>자바스크립트 object 자료형이랑 비슷함

![](assets/Node.js%20&%20MongoDB%201-55.png)
- ▲ 그래서 이렇게 생긴 document를 두개 정도 만들어봤습니다.

- **Q. 근데 document 하나에 여러 게시물 보관해도 되는거 아님?**<br>그래도 되긴 되는데 <br>MongoDB쓸 때 중요한 점이 하나 있는데<br>document는 100만개 있어도 **document 1개 찾는건 매우 빠릅니다.** 

- 근데 document 하나 안에 100만개의 문장이 있고 거기서 원하는 문장하나만 찾는건 매우 어렵습니다. <br>그래서 각각 document에 게시물 1개 씩만 저장해두는게 나을거같군요.<br>다르게 설명하면 document는 하나의 엑셀 행이라고 생각하면 됩니다<br>저번엔 파일이라고 했던거같은데 더 정확히 말하면 엑셀 행입니다.

![](assets/Node.js%20&%20MongoDB%201-56.png)

- ▲ 하나의 엑셀 행에다가 이렇게 자료 저장하는사람 있어요?<br>아마 없습니다.

![](assets/Node.js%20&%20MongoDB%201-57.png)
- ▲ 이렇게 한줄한줄 저장하는게 좋습니다.<br>document도 마찬가지로 엑셀의 행 하나라고 생각하고 저장하면 나중에 별 문제 없습니다.

![](assets/Node.js%20&%20MongoDB%201-48.png)    

#### `_id`, ObjectId 가 뭐냐면
![](assets/Node.js%20&%20MongoDB%201-58.png)

- ▲ document 만들 때 잘 보시면 `_id` 라는 항목도 자동생성된걸 볼 수 있습니다<br>`_id`는 document마다 구분하기 위한 유니크한 번호입니다. <br>왜냐면 예를 들어 유저 두명이 똑같은 글을 써버리면 구분이 안되기 때문에 <br>자동으로 유니크한 `_id` 같은걸 자동으로 부여해줍니다.<br>그냥 글번호라고 생각해도 될거같습니다.

- 그리고 `_id`에는 1, 2, 3 이런 정수가 아니라<br>기본적으로 ObjectId 라고 부르는 랜덤 문자를 집어넣어줍니다. 

- ObjectId의 특징은
	- 서로 중복되지 않고 
	- 먼저만든 document가 더 빠른, 그니까 숫자가 낮은 ObjectId를 가지고 있습니다.
	- 자동부여가 싫으면 ObjectId 대신 직접 1, 2, 3 이렇게 숫자를 넣어도 전혀상관없습니다. 
- 근데 귀찮으니까 보통은 자동부여된거 그대로 냅둡니다.

![](assets/Node.js%20&%20MongoDB%201-49.png)


#### 페이지 방문시 DB 데이터 보여주기
- 예를 들어 /list 페이지에 방문하면 DB에 있던 글을 뽑아서 보여주고 싶으면 어떻게하는지 알아봅시다.
```js
app.get('/list', (요청, 응답) => {
  응답.send('안녕')
})
```

- 유저가 /list 페이지 방문하면 뭔가 보내주고 싶으면<br>이런거 코드짜면 된다고 했습니다.<br>근데 '안녕' 말고 DB에 있던 글을 뽑아서 보내주고 싶으면요?

```js
await db.collection('컬렉션명').find().toArray() 
```

- DB에 있던 데이터를 하나 꺼내고 싶으면 이런거 쓰면 됩니다.<br>그럼 이 자리에 컬렉션에 있던 모든 document가 출력됩니다.

```js
app.get('/list', async (요청, 응답) => {
  let result = await db.collection('컬렉션명').find().toArray()
  응답.send(result[0].title)
})
```

- 그래서 이렇게 코드짜면 유저가 /list 페이지 방문하면 DB에 있던 첫글 제목을 보내줍니다. <br>참고로 await 쓰려면 그 전에 async라는걸 콜백함수 왼쪽에 붙여야합니다.

##### await이 뭐임
- await이 뭐냐면 다음 줄 실행하기 전에 잠깐 기다리라는 뜻입니다.<br>왜 이게 필요하냐면 **자바스크립트는 참을성이 없습니다.**<br>자바스크립트에서 처리가 좀 오래걸리는 함수들은<br>가끔 처리가 완료되기까지 기다리지 않고 바로 다음 줄을 급하게 실행하려고 하기 때문에 (일명 비동기처리)<br>그걸 막고 싶으면 _콜백함수를 쓰거나 await을 쓰거나 .then을 쓰거나 셋 중 하나_ 쓰면 됩니다.

```js
app.get('/list', async (요청, 응답) => {
  let result = db.collection('컬렉션명').find().toArray()
  응답.send(result[0].title)
})
```

- 그래서 db.collection() 어쩌구 코드들은 처리가 좀 오래걸리기 때문에<br>그런 코드에 await을 안써버리면 DB에서 데이터 꺼내오기도 전에 응답.send() 를 실행해버립니다. <br>그래서 await 붙여야합니다.<br>실은 그냥 mongodb 라이브러리에서<br>db.collection().어쩌구() 코드들은 항상 await을 붙이라고 하기 때문에 그렇게 쓴 것이라고 생각해도 됩니다.

- 예전 버전의 mongodb 라이브러리는 .then() 아니면 콜백함수를 넣어서 작성했었습니다. <br>근데 await 쓰면 더 깔끔해보이니까 그걸로 쓰도록 합시다. 

- 참고로 await도 여러분 맘대로 붙이는게 아니라 붙일 수 있는 곳만 붙일 수 있습니다.<br>정확히 말하면 Promise를 뱉는 곳에다가만 붙일 수 있는데<br>당연히 mongodb 라이브러리 만든 사람이 여기다가 await 붙일 수 있게 만들어놔서 이게 가능한거니까 참고합시다.

```js
app.get('/list', async (요청, 응답) => {
  db.collection('컬렉션명').find().toArray().then((result)=>{
    응답.send(result[0].title)
  })
})

app.get('/list', async (요청, 응답) => {
  db.collection('컬렉션명').find().toArray((err, result)=>{
    응답.send(result[0].title)
  })
})
```

![](assets/Node.js%20&%20MongoDB%201-50.png)

![](assets/Node.js%20&%20MongoDB%201-51.png)

#### array/object 자료형
- array와 object 자료형인데 이런거 미리배워오랬는데<br>무시하고 그냥 듣는 분들도 있기 때문에 잠깐 설명하자면 <br>자바스크립트에서 여러가지 자료들을 변수하나에 저장하고 싶으면 <br>array자료형을 사용하면 됩니다

```js
let a = [10, 20, 30]
```
- 이러면 변수 하나에 여러가지 숫자나 문자를 담아서 보관할 수 있습니다.

```js
let a = [10, 20, 30]
console.log(a[1])
```

- 나중에 원하는 자료만 쏙 빼서 사용하고 싶으면 <br>변수명 뒤에 대괄호 치고 몇번째 자료를 꺼내고 싶은지 써주면 됩니다.<br>위의 코드에서 `[1]` 이라고 쓰면 1번째 자료가 나옵니다. <br>컴퓨터는 0부터 세기 때문에 아마 20이 출력됩니다. 확인해봅시다. 

- array자료형이 못생겨서 싫으면 object 자료형도 있습니다.<br>object자료형도 똑같이 여러 자료를 변수하나에 쑤셔박아두고 싶을 때 씁니다.
```js
let b = { name : 'kim', age : 20 }
```

- { } 열고 자료들을 콤마로 구분해서 넣으면 되는데<br>차이점이 하나 있는게 object는 자료마다 왼쪽에 이름을 지어줘야합니다.<br>그래서 저는 이름과 나이를 한번 저장해봤습니다

```js
let b = { name : 'kim', age : 20 }
console.log(b.name)
console.log(b['name'])
```

- 나중에 자료하나만 쏙 꺼내고 싶으면 object 자료 오른쪽에 점찍고 자료이름 집어넣으면 됩니다.<br>그럼 그 자료만 쏙 뽑아낼 수 있습니다.<br>점찍기 싫으면 `['자료이름']` 넣어도 됩니다.

#### 저는 첫 글의 제목만 꺼내고 싶은데요 
- DB에서 가져온 결과를 result 변수같은 것에 담아서 출력해보면 <br>대괄호랑 중괄호가 이상하게 섞여있습니다.

```js
[
  {
    _id : new ObjectId('어쩌구'),
    title : '첫게시물',
    content : '내용임 111'
  },
  {
    _id : new ObjectId('어쩌구'),
    title : '두번째글임',
    content : '안녕'
  },
]
```

- DB에서 출력한 자료도 array와 object를 활용해서 데이터를 보여줍니다. <br>이상하고 복잡하게 생겼지만 쉽게 설명하면 array 안에 object 몇개를 넣어뒀을 뿐입니다.<br>`[ { }, { } ]` 대충 이렇게 생긴 자료입니다. <br>실은 array 안에 object 맘대로 넣을 수 있습니다.

- 그럼 result 변수에 저렇게 글들이 저장되어있는데<br>거기서 **첫 글의 제목**만 뽑고 싶으면 어떻게 코드짜면 될까요?<br>-> 아무리 복잡하게 생긴 자료도 시작 괄호만 잘 보면 원하는 내용만 쉽게 뽑을 수 있습니다.

- result 출력해보면 시작괄호가 뭐죠? <br>각진 `[ ]` 대괄호죠? <br>그럼 무조건 array 자료라서 array에서 자료뽑는 문법부터 쓰면 됩니다.

```js
app.get('/list', async (요청, 응답) => {
  let result = db.collection('컬렉션명').find().toArray()
  console.log(result[0])
})
```
- 그래서 이거 실행해보면 (/list 페이지 방문해보면)

```js
{
  _id : new ObjectId('어쩌구'),
  title : '첫게시물',
  content : '내용임 111'
}
```

- 이런게 터미널에 출력됩니다. <br>이 자료는 { } 중괄호로 시작하죠?<br>그럼 대부분 object 자료라서 object 자료에서 자료 뽑는 문법 쓰면 됩니다.

```js
app.get('/list', async (요청, 응답) => {
  let result = db.collection('컬렉션명').find().toArray()
  console.log(result[0].title)
})
```

- 그래서 이거 실행해보면 첫 글의 제목만 잘 출력되는군요. <br>심심하면 둘째 글제목도 한번 뽑아서 출력해보시길 바랍니다 

```ad-note
오늘 배운거 정리하자면 

1. 컬렉션에 있던 document 전부 꺼내고 싶으면 `db.collection('컬렉션명').find().toArray()`

2. array자료에서 자료뽑고 싶으면 `array자료[자료순서]` 

3. object자료에서 자료뽑고 싶으면 `object자료.자료이름` 

4. 일부 늦게 동작하는 코드들은 `await` 안붙이면 그 다음줄부터 실행됨 
```

- 다음 시간엔 이 데이터들을 html 웹페이지에 집어넣는 방법을 알아보도록 합시다 <br>그래야 유저가 볼 수 있을거아닙니까

![](assets/Node.js%20&%20MongoDB%201-52.png)

![](assets/Node.js%20&%20MongoDB%201-53.png)


### 웹페이지에 DB데이터 꽂기 (EJS, 서버사이드 렌더링)
- 저번시간에 DB에서 출력한 글제목을 유저에게 보내주는건 성공했는데 <br>근데 데이터만 달랑 보내면 되겠습니까<br>멋진 글목록페이지를 html로 하나 만들어서<br>그 안에 글제목들을 박아넣어서 유저에게 그 html  페이지를 보내보도록 합시다. 

- 근데 그러려면 html안에 데이터를 꽂아넣는 법을 알아야하는데 그건 템플릿 엔진이라는걸 쓰면 가능합니다.<br>그거쓰면 html 안에다가 서버에 있던 데이터들을 막 꽂아줄 수가 있습니다 <br>템플릿엔진은 여러가지중에 고를 수가 있는데 우리는 이 중에서 가장 쉽고 간단한 ejs를 써볼 것입니다. <br>다른 템플릿엔진들은 새로운 문법 많이 익혀야되는데 이건 딱히 새로운 문법 익힐 필요없이 자바스크립트 문법그대로 사용할 수 있음

![](assets/Node.js%20&%20MongoDB%201-60.png)

#### ejs 셋팅
- 템플릿엔진을 쓰려면<br>터미널 열어서 npm install ejs 입력해주고 

```js
app.set('view engine', 'ejs') 
```

- 그 다음에 서버파일 상단쯤에 view engine을 쓰겠다고 위처럼 적어봅시다. <br>왜냐고요? express 만든 사람이 이래야 ejs 템플릿 엔진을 쓸 수 있다고 하는군요. <br>그럼 이제 ejs를 이용해서 html 파일안에 데이터들을 막 꽂아줄 수 있습니다.

#### list.ejs 파일 만들고 보내주기 
- html 파일 안에 데이터를 꽂아넣고 싶으면<br>`.ejs` 파일을 만들어서 거기에 데이터를 꽂아넣으면 그걸 자동으로 html로 변환해줍니다.
![](assets/Node.js%20&%20MongoDB%201-64.png)

- 근데 ejs 파일들은 전부 views라는 폴더만들어서 거기 보관하셔야합니다.<br>그래서 저는 거기에 list.ejs를 만들어봤습니다. <br>ejs 파일은 어려운거 없고 기본적으로 html이랑 똑같이 작성하면 됩니다.<br>근데 안에 살짝씩 ejs 문법써서 서버데이터를 집어넣을 수 있다는것만 다름 

- 그래서 글목록페이지같은걸 만들고 싶으니<br>거기맞는 레이아웃 디자인을 넣어보도록 합시다.

##### list.ejs 파일에 넣을 웹페이지 디자인
```html
<body class="grey-bg">

  <div class="white-bg">
    <div class="list-box">
      <h4>글제목임</h4>
      <p>글내용임</p>
    </div>
    <div class="list-box">
      <h4>글제목임</h4>
      <p>글내용임</p>
    </div>
  </div> 

</body>
```

```css
.grey-bg {
  background: #eee;
}
.white-bg {
  background: white;
  margin: 20px;
  border-radius: 5px;
}
.list-box {
  padding : 10px;
  border-bottom: 1px solid#eee;
}
.list-box h4{
  font-size: 16px;
  margin: 5px;
}
.list-box p {
  font-size: 13px;
  margin: 5px;
  color: grey;
}
```

```js
app.get('/list', (요청, 응답) =>{
  응답.render('list.ejs')
})
```

- 이제 /list 방문하면 이거 글목록페이지 보내주면 좋을거같으니까<br>방금만든 ejs 페이지를 유저에게 보내줘보도록 합시다. <br>ejs파일을 유저에게 보내주고 싶으면 `응답.sendFile` 이런게 아니라<br>`응답.render`라고 쓰고 안에 views안에 있던 ejs 파일의 경로 집어넣어주면 됩니다. 

- 진짜 잘 나오나 /list 페이지 방문해서 테스트해봅시다. 
#### 데이터 넣는 법 
- 이제 서버에 있던 DB 데이터를 list.ejs 집어넣어주면 글목록 페이지가 완성될거같은데<br>서버 데이터를 list.ejs 파일에 넣고 싶으면 두가지 스텝이 있습니다 
	1. 일단 ejs 파일로 데이터를 보내고 
	2. ejs 파일 안에서 ejs 문법써서 데이터를 원하는데 꽂으면 됩니다.

```js
app.get('/list', async (요청, 응답) => {
  let result = await db.collection('post').find().toArray()
  응답.render('list.ejs', { 글목록 : result })
})
```

1. ejs파일로 데이터 보내는 법은<br>`응답.render()` 의 둘째 파라미터에 `{ 작명 : 전송할데이터 }` 이렇게 적으면 ejs 파일로 데이터가 전달됩니다.<br>위의 코드는 글목록이라는 이름으로 result안에 들은게 전달되겠군요. 

 ```js
 <%= 글목록 %>
```
2. 이제 ejs 파일 안에서 <%= %> 문법 안에 아까 작명한걸 담으면 그걸 출력해볼 수 있습니다.

```js
(list.ejs 파일 아무데나)
<%= JSON.stringify(글목록) %>
```

- 근데 실은 array나 object 데이터를 그대로 html에 박을 경우 `JSON.stringify()` 안에 적어야 안깨지고 잘보입니다. <br>한번 /list 페이지 방문해서 진짜 글목록이 나오나 확인해봅시다.

![](assets/Node.js%20&%20MongoDB%201-65.png)

  - ▲ DB 데이터들이 잘 나오는군요. <br>근데 이 복잡한 자료형에서 첫째 제목만 뽑아서 원하는 곳에 집어넣고 싶으면 어떻게 하죠?

```html
(list.ejs)

<div class="white-bg">
  <div class="list-box">
    <h4><%= 글목록[0].title %></h4>
    <p>글내용임</p>
  </div>
  <div class="list-box">
    <h4>글제목임</h4>
    <p>글내용임</p>
  </div>
</div> 
```

- `글목록[0].title` 이러면 첫 글의 제목이 잘 나오겠군요.<br>array, object에서 데이터뽑는건 저번에 한 내용이니 설명은 생략하도록 합시다. <br>허전하니까 글내용도 html에 박아보시길 바랍니다.<br>둘째글의 제목이랑 내용도 html에 박아보십쇼 


#### 서버사이드 렌더링 
- 참고로 **서버사이드 렌더링**이라는 멋있는 말이 있습니다.  <br>html을 서버측에서 데이터채워서 완성해서 유저에게 보내주는걸 서버사이드렌더링이라고 멋있게 부르구요 <br>우리가 지금하고 있는 짓거리입니다.

- 뭐 다른 방법도 있냐고요? <br>다른 방법은 **클라이언트사이드 렌더링**이라는것도 있습니다<br>html을 서버에서 만들어서 보내는게 아니라 <br>텅 비어있는 html과 데이터만 유저에게 보내고<br>html 내용은 자바스크립트로 유저 브라우저에서 생성하는겁니다. 

- 이 경우 장점은 모바일 앱처럼 부드러운 사이트를 만들 수 있다는게 장점입니다.<br>리액트 쓰면 클라이언트사이드 렌더링이 쉬워집니다. <br>한 때 클라이언트사이드 렌더링이 유행이어서 모든걸 다 리액트써서 그렇게 만들려고 했는데
	1. 웹페이지가 무거워져서 퍼포먼스도 안좋아지고 
	2. SEO도 안좋다는 단점 때문에 
- 다시 서버사이드 렌더링이 주목받고 있습니다. <br>물론 기호에 따라서 섞어서 쓸 수도 있습니다. 
- 개인적으로 서버사이드 렌더링으로 모든걸 만드는데<br>html에서 꼭 필요한 일부만 클라이언트사이드 렌더링하는게 합리적인 것 같습니다.

```ad-note
오늘의 결론은 

1. html 파일안에 서버데이터 넣어서 보내주고 싶으면 템플릿엔진쓰면 되는데 ejs를 썼음 

2. 응답.render( ) 문법으로 ejs 파일로 서버에 있던 데이터를 전송할 수 있고 

3. ejs 파일 안에서 아무데나 <%= 서버가보낸데이터이름 %> 쓰면 서버가 보낸 데이터가 html안에 보입니다. 


```


```ad-tip
- 오늘 배운거 
1. ejs쓰면 html 안에 서버데이터 꽂기 가능
2. ejs 파일은 views 폴더 안에 만들고
3. 응답.render로 유저에게 보낼 수 있음
4. ejs파일로 서버데이터 전송하고<br><%=데이터명%> 써서 html에 박아넣기 가능
```

```ad-todo
오늘의 숙제 : 

/time 이라고 접속하면 현재 서버의 시간을 보내주는 기능을 만들어봅시다.

ejs로 웹페이지를 만들어서 거기 안에 서버의 시간을 박아넣어서 보내주면 될 것 같군요. 

(팁) 서버의 시간은 server.js 파일 아무데서나 new Date() 라고 쓰면 나옵니다
```


