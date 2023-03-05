### Python 기초

#### intro
- 컴퓨터(**Compute**r)
	- **Calculation + Remeber**
- 프로그래밍(**program**ming)
	- **명령어의 모음(집합)**

- 언어?
	- 자신의 **생각을 나타내고 전달하기** 위해 사용하는 체계
	- **문법적**으로 맞는 말의 집합
- 프로그래밍 언어?
	- 컴퓨터에게 명령하기 위한 약속

- 선언적 지식(declarative knowledge)
	- "사실에 대한 내용"
- **명령적 지식(imperative knowledge)**
	- **"How-to"**


### 파이썬 개발 환경 (Python Enviroment)

#### 파이썬 (Python) 이란?
- Easy to learn
	- 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않음
		- 예시 : 변수에 별도의 타입 지정이 필요없음
	- 문법 표현이 매우 간결하여 프로그래밍 경험이 없어도 짧은 시간 내에 마스터할 수 있음
		- 예시 : 문장을 구분할 때 중괄호 ({,}) 대신 들여쓰기를 사용

- Expressive Language
	- 같은 작업에 대해서도 C나 Java로 작성할 때 보다 더 간결하게 작성 가능

```java

public class HelloPython {
	public static void main(String[] args){
		System.out.println("Hello Python!");
	}
}
```

```python
print('Hello Python!')
```

- 크로스 플랫폼 언어
	- windows, mac OS, Linux, Unix 등 다양한 운영체제에서 실행 가능

- 인터프리터 언어(Interpreter)
	- 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
	- 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음
```python
>>> 2 + 2 # 사용자가 입력(input)
4         # 컴퓨터가 대답(output)
```

- 객체 지향 프로그래밍(Object Oriented Programming)
	- 파이썬은 객체 지향 언어이며, 모든 것이 객체로 구현되어 있음
		- 객체(Object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

#### 파이썬 개발환경
1. 파이썬 기본 인터프리터 : IDLE
	- IDLE (intergrated Development and Learning Enviroment)
		- 내장 프로그램으로 파이썬 설치 시 기본적으로 설치 → 인터프리터가 대화형 모드로 동작함
			- 여러 줄의 코드가 작성되는 경우 보조 프롬프트(`...`)가 사용됨
			- 프롬프트(`>>>`)에 코드를 작성하면 해당 코드가 실행됨
		- Python이 설치된 환경에서는 기본적으로 활용 가능하나 디버깅 및 코드 편집, 반복 실행이 어려움

2. Python 스크립트 실행
	- IDE(ex) Pycharm), Text Editor(ex) VS Code)등에서 작성한 파이썬 스크립트 파일을 직접 실행



### 기초 문법
#### 코드 스타일 가이드 
- 코드를 '어떻게 작성할지'에 대한 가이드라인
- 파이썬에서 제안하는 스타일 가이드
	- PEP8 (https://peps.python.org/pep-0008/)
- 기업, 오픈소스 등에서 사용되는 스타일 가이드
	- Google Style guide (https://google.github.io/styleguide/pyguide.html)


#### 들여쓰기 (Indentation)
- Space Sensitive 
	- 문장을 구분할 때, 들여쓰기(Indentation)를 사용
	- 들여쓰기를 할 때는 4칸(`space`키 4번) 혹은 1탭(`Tab`키 1번)을 입력
		- 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용 → 혼용하면 안됨
			- Tab으로 들여쓰면 계속 탭으로 들여써야 함
			- 원칙적으로는 공백(빈칸, `space`) 사용을 권장[^python-01-01]

25page 부터

[^python-01-01]: PEP8 권장사항