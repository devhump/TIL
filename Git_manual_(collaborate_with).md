## Git 으로 협업하기 

### 0. git 레포지토리 생성

#### 원격 레포지토리 생성 후 collaborator 초대

#### 가상환경 설정 
```bash
$ python -m venv venv
```

####  `.gitignore` 생성
📌 가상환경 (venv)을 이용해 개발을 진행하려는 경우, 

반드시 `git init` 이전에 `venv` 를 포함한 `.gitignore` 을 생성해야함 

- [gitigore.io](https://www.toptal.com/developers/gitignore/)
> python, django, vscode, windows, mac 등


#### 로컬 저장소와 원격 저장소 연결
```bash
# 저장소 초기화
$ git init
	
#
$ git remote add origin [원격 저장소 주소]
	
```

---

### A. Github 저장소 Mirror

#### 1-1. 깃허브 새로운 저장소 생성

- 2번 개발자는 새로운 저장소를 생성합니다.

#### 1-2. 1번 개발자 저장소 clone 하기

- 2번 개발자는 1번 개발자의 저장소를 clone 합니다

```bash
git clone --mirror {1번 개발자 페어 프로그래밍 저장소 주소}
cd {1번 개발자의저장소이름}
```

#### 1-3. 복사한 저장소의 원격 저장소 설정

- 2번 개발자는 새롭게 생성한 원격 저장소를 복사해온 프로젝트의 원격 저장소로 설정합니다.

```bash
git remote set-url --push origin {2번 개발자의 새롭게 생성한 저장소 주소}
```

#### 1-4. push

- 2번 개발자는 프로젝트를 Push 합니다.

```bash
git push --mirror
```