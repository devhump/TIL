---
alias: 'VS Code를 이용한 파이썬 소스코드 디버깅'
tags: [vscode, debugging]
---


- 참조 영상 👉 https://youtu.be/GEGXVzegNew

### VS code 디버깅 관련 단축키
|     단축키     |             기능             |
|:--------------:|:----------------------------:|
|      `F9`      |         break point          |
|      `F5`      |         디버깅 실행          |
| `ctrl` + `F5`  |       디버깅 없이 실행       |
|     `F10`      |    인터프리터 한 줄 이동     |
|     `F11`      |        함수 안 디버깅        |
| `shift` + `F5` | 디버깅 모드 종료 (실행 취소) |


### WATCH 패널 활용
- 처음에는 비어져 있는데, 여기에 내가 **원하는 변수명을 입력**하면(코드 내에 쓰이는) ***디버깅 과정에서 변화되는 변수의 값을 확인***할 수 있다. 
	- ![](_others_/assets/debugging%20with%20vs%20code.png)

- 👇 아직 해당 변수에 값이 할당되지 않았으면 에러가 발생한다.
	- 👉 어떤 코드 라인에서 변수가 할당되는지 알 수 있다. 
		- ![](_others_/assets/debugging%20with%20vs%20code-1.png)