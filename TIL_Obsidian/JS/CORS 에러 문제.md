---
title : 
aliases : 
tags : [JS, error]
---

![](assets/CORS%20에러%20문제.png)

```
Access to script at 'file:///C:/Users/Ramy/Desktop/moonbucks-menu/src/js/index.js' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, isolated-app, chrome-extension, chrome, https, chrome-untrusted.
```

- CORS 문제가 발생해서 로컬에서 자바스크립트 코드를 실행할 경우 작동하지 않는 경우가 있다.

### 해결방법
- 기본적으로 로컬에서 발생하는 문제로, 서버에서 구동을 하면 문제없이 실행된다고 한다. 하지만, 개발 단계에서의 편의상 로컬에서 구동할 수 있는 방법을 정리해 본다. 

#### 1. 브라우저의 보안 해제 
1. 바탕화면에 브라우저(크롬) 바로가기를 만든다.
2. 해당 아이콘 우클릭 → 속성을 누른다.
3. 속성 창에 `--disable-web-security --user-data-dir=%LOCALAPPDATA%\Google\chromeTemp -–allow-file-access-from-files` 를 추가로 입력한 후 적용한다. 
4. 보안에 문제가 발생할 수 있다고 안내 문구가 뜨나, JS 코드는 제대로 작동한다. 

```
* 입력전 내용
"C:\Program Files\Google\Chrome\Application\chrome.exe" 

* 입력 후 
"C:\Program Files\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir=%LOCALAPPDATA%\Google\chromeTemp -–allow-file-access-from-files
```
![](assets/CORS%20에러%20문제-1.png)
![](assets/CORS%20에러%20문제-2.png)

![](assets/CORS%20에러%20문제-3.png)

![](assets/CORS%20에러%20문제-4.png)


#### 2. VS Code extention을 사용한다. 
- VS Code extention 중 Live server를 설치한다. 
- 명령어 팔레트에서 `live server: Open with live Server`를 실행한다. 
	- 또는 우측 하단 줄에서 `Go live` 를 클릭한다.
![](assets/CORS%20에러%20문제-5.png)


![](assets/CORS%20에러%20문제-6.png)

![](assets/CORS%20에러%20문제-7.png)

![](assets/CORS%20에러%20문제-8.png)


#### 3. npm - live-server를 사용한다.  
- npm 사용을 위해 [node.js](https://nodejs.org/en)를 설치한다.

```ad-tip
- 이때, 설치가 잘 되었는지 확인 하는 방법
	- cmd(또는 터미널)에서 `node -v`, `npm -v`를 입력했을 때 버전이 표시되면 제대로 설치된 것이다.
![](assets/CORS%20에러%20문제-9.png)
```

- 이후 live-server를 설치한다. 
```node
npm install -g live-server
```

- 실행은 해당 폴더에서 터미널 → `live-server` 를 입력한다. 
```shell
# 또는 
live-server 폴더명
```

![](assets/CORS%20에러%20문제-10.png)

- 이후 디폴트 브라우저가 뜨면서 자동으로 해당 프로젝트가 실행된다.