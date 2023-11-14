---
tags:
  - Linux
---
```dataview
list from #HomeServer
```
### tldr
- **tldr** InBrowser.App 👉 https://tldr.inbrowser.app/

#### 테마 변경
- https://github.com/tldr-pages/tldr-node-client#configuration

```shell
cd
sudo vim .tldrrc
```

- `.tldrrc` 파일에 해당 내용 입력
```shell
{
  "themes": {
    "ocean": {
      "commandName": "bold, cyan",
      "mainDescription": "",
      "exampleDescription": "green",
      "exampleCode": "cyan",
      "exampleToken": "dim"
    },
    "myOwnCoolTheme": {
      "commandName": "bold, red",
      "mainDescription": "underline",
      "exampleDescription": "yellow",
      "exampleCode": "underline, green",
      "exampleToken": ""
    }
  },
  "theme": "ocean"
}
```

#### tldr 참고문서
- https://github.com/tldr-pages/tldr
- https://tldr.sh/
- [# Linux man 페이지의 단점을 해결하는 TL;DR 프로젝트](https://www.lesstif.com/lpt/linux-man-tl-dr-66715656.html)

### exa
- 현대판 ls
- 훨씬 빠른 조회와 컬러풀한 출력을 지원
- git과 통합되어 있어 파일의 버전 상태도 같이 표시
- https://the.exa.website/features
- [# exa 명령어 사용법 (ls 대신 이거 쓰자)](https://inpa.tistory.com/entry/Modern-Linux-%F0%9F%90%A7-exa-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%82%AC%EC%9A%A9%EB%B2%95-ls-%EB%8C%80%EC%8B%A0-%EC%9D%B4%EA%B1%B0-%EC%93%B0%EC%9E%90)
```shell
exa [옵션] [파일]
exa --help

exa
exa -lh --icons

$ exa --classify # 각 파일이 실행 파일인지, 디렉터리인지, socket 인지, link 인지 여부를 표시
$ exa -F # 위와 같음

$ exa -T # 트리 구조로 보기
$ exa -T -L=2 # 트리 구조로 보기 (2단계 가지 까지만)
```

```shell
ls
l 
ll # long list
la # list all
```

### fzf
#### git을 이용한 설치
```shell
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

#### 업데이트 (git 방식)
```shell
cd ~/.fzf && git pull && ./install
```

#### 실행
```shell
fzf
```
- **위 명령어로 출력되는 내용이 적다면, 상위 폴더에서 실행해보자**

![](assets/Linux%20최신%20명령어.png)
#### key binding
- `ctrl + t` : 커맨드 상에서 파일들 혹은 디렉토리를 찾을때!
- `ctrl + r` : 커맨드상에서 입력했던 history search
- `alt + c` : 현재 디렉토리 기준으로 이동하기
	- 파일 위치 가져오기와 비슷하지만 선택하면 자동으로 cd 명령어가 적용되어 이동합니다

#### 와일드 카드(`**`)와 함께 사용하기
```shell
ssh **<TAB> => ssh 목록(~/.ssh/config) 보여주기
kill **<TAB> => 닫을 프로세스 선택하기
vim ./fzf/**<TAB> => fzf 폴더 내부의 목록만 보여주기
cd ../**<TAB> => 부모폴더 기준으로 fuzzy 실행하기
```

#### search syntax
- `weekly-news` > 퍼지 매칭
- `^weekly-news` > 접두사 완전 매칭
- `.md$` > 접미사 완전 매칭
- `'md` > 완전 매칭
- `!.md` > 역완전매칭
- `!.md$` > 역-접미사 완전 매칭

#### fzf 참고문서
- https://github.com/junegunn/fzf
- [# 오라클 A1 우분투에서 fzf 단축키 안될 때 해결 방법](https://bonik.me/967/)
- [FZF로 ZSH 터미널 더 강력하게 사용하기](https://medium.com/harrythegreat/fzf%EB%A1%9C-zsh-%ED%84%B0%EB%AF%B8%EB%84%90-%EB%8D%94-%EA%B0%95%EB%A0%A5%ED%95%98%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-730c20eb496b)
- https://www.linode.com/docs/guides/how-to-use-fzf/

### duf (최신식 df)
- 마운트된 디스크 파일의 크기와 용량을 다채롭게 보여주는 최신식 명령어
- 사용자 친화적인 다채로운 출력
- 터미널의 테마 및 너비에 맞게 조정
- 필요에 따라 결과 정렬
- 그룹 및 필터 장치
- JSON을 편리하게 출력
- https://github.com/muesli/duf

### fd (최신식 find)
https://github.com/sharkdp/fd#installation

![](assets/Linux%20최신%20명령어-1.png)

```shell
export PATH=$PATH:/home/ramy/.local/bin
export PATH="$HOME/.local/bin:$PATH"
```

.bashrc
PATH=$PATH:/home/ramy/.local/bin

### nnn (최신 mv/cp/mkdir)
- 터미널 파일 매니저 (터미널에서 쓰는 탐색기라고 보면 된다)
- 보통 mv, cp, mkdir 등등 명령어를 개별로 써야하는데 nnn 속에서 단축키로 여러 작업 가능
- https://github.com/jarun/nnn

### 참고문서
- [# Modern Linux - 최신식 리눅스 명령어 모음](https://inpa.tistory.com/entry/LINUX-%F0%9F%93%9A-%EB%AA%A8%EB%8D%98-%EB%A6%AC%EB%88%85%EC%8A%A4-%ED%84%B0%EB%AF%B8%EB%84%90%EC%9D%84-%ED%99%94%EB%A0%A4%ED%95%98%EA%B2%8C-%F0%9F%90%A7-%EC%B5%9C%EC%8B%A0%EC%8B%9D-CLI-%EB%AA%A8%EC%9D%8C#fd_%EC%B5%9C%EC%8B%A0%EC%8B%9D_find)
