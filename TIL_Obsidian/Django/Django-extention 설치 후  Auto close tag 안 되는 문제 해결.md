---
title : 
aliases : 
tags : [error, vscode]
---

![](assets/Django-extention%20설치%20후%20%20Auto%20close%20tag%20안%20되는%20문제%20해결-2.png)

![](assets/Django-extention%20설치%20후%20%20Auto%20close%20tag%20안%20되는%20문제%20해결-1.png)

- vs code 에서 Auto Close Tag를 잘 쓰고 있는데, Django extension을 설치하면 장고 문법 사용시 자동으로 'django-html' 문법으로 인식하여 작동하지 않는 경우가 더러 있다.  

![](assets/Django-extention%20설치%20후%20%20Auto%20close%20tag%20안%20되는%20문제%20해결-3.png)

- vs code 우측 하단에 보이는 저 표시가 바로 그것인데, 이때, HTML 을 사용하면 제대로 작동하나, 장고 문법이 제대로 syntax highlighting 되지 않는 문제가 발생한다. 


### 1. VS code → 설정 → emmet 설정
- 여기서 아래 항목을 추가한다. 
	- 항목 : django-html
	- 값 : html
![](assets/Django-extention%20설치%20후%20%20Auto%20close%20tag%20안%20되는%20문제%20해결.png)

- 👉 이렇게 되면 `div` 를 누르고 tab을 누르면 `<div></div>` 구문이 완성된다. 

### 2.  settings.json 에 아래 내용을 추가한다. 
```
    "auto-close-tag.activationOnLanguage": [
        "django-html",
    ],
```

- 👉 이후에는 기존의 html에서와 같이 auto close tag 기능이 활성화가 된다 .


###### 출처: https://stackoverflow.com/questions/61744003/how-can-i-autocomplete-both-html-and-django-html-simultaneously-in-visual-studio