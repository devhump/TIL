---
tags:
  - Linux
  - HomeServer
---


- vim 의 설정값은 `.vimrc` 파일을 수정함으로변경할 수 있고, <br>`.vimrc` 파일은 언제나 홈 디렉토리에 존재해야 한다.

```shell
vim ~/.vimrc
```

```vim
" Syntax Highlighting    
if has("syntax")    
	syntax on    
endif  
  
set number "set nu 동일, 줄번호 표시를 해줍니다.  
  
" Auto Indent  
set autoindent " (set ai) 자동 들여쓰기  
set cindent " c style indent  
  
" Set Tab Indent  
set smartindent "줄바꿈 시, 이전 문장의 indent에서 새로 시작  
set shiftwidth=4 "자동 들여쓰기(auto indent)할 때의 너비  
set tabstop=4 "tab을 4칸으로  
set expandtab "tab안에 space 채우기  
set smarttab  
  
" status line  
set ruler " 상태표시줄에 커서의 위치 표시  
set showcmd " show (partial) command in status line  
set laststatus=2 " 상태바 표시를 항상한다    
set statusline=\ %<%l:%v\ [%P]%=%a\ %h%m%r\ %F\  
set autowrite " 다른 파일로 넘어갈 때 자동 저장    
set autoread " 작업 중인 파일 외부에서 변경됬을 경우 자동으로 불러옴  
  
set paste " 붙여넣기 계단현상 없애기  
  
set nocompatible   " 방향키로 이동가능  
set fileencodings=utf-8,euc-kr " 파일인코딩 형식 지정  
set bs=indent,eol,start " backspace 키 사용 가능  
set history=1000  " 명령어에 대한 히스토리를 1000개까지  
set nobackup  " 백업파일을 만들지 않음  
set title " 제목을 표시  
set showmatch " 매칭되는 괄호를 보여줌  
set nowrap " 자동 줄바꿈 하지 않음  
set wmnu " tab 자동완성시 가능한 목록을 보여줌
set mouse=a " 마우스 위치로 커서 이동
  
"가장 최근에 수정한 곳에 커서 위치    
au BufReadPost *    
\ if line("'\"") > 0 && line("'\"") <= line("$") |    
\ exe "norm g`\"" |    
\ endif  
  
" color scheme 사용  
set t_Co=256  
colorscheme jellybeans
```

```shell
if has("syntax")    
	syntax on    
endif  
  
set number
  
set autoindent 
set cindent
  
" Set Tab Indent  
set smartindent  
set shiftwidth=4
set tabstop=4 
set expandtab  
set smarttab  
  
set ruler
set showcmd 
set laststatus=2    
set statusline=\ %<%l:%v\ [%P]%=%a\ %h%m%r\ %F\  
set autowrite   
set autoread
  
set paste  
  
set nocompatible
set fileencodings=utf-8,euc-kr  
set bs=indent,eol,start  
set history=1000  
set nobackup  
set title 
set showmatch
set nowrap
set wmnu
set mouse=a
  
au BufReadPost *    
\ if line("'\"") > 0 && line("'\"") <= line("$") |    
\ exe "norm g`\"" |    
\ endif  
  
set t_Co=256  
colorscheme jellybeans

```
- mac  에서는 colorscheme 이 금방 적용됐는데, linux 환경에서는 적용이 안되서 한참 고생 했었다.
	- 👉 `.vimrc` 파일에 `set t_Co=256` 내용을 추가하니 바로 해결됨...

#### colorscheme 설정방법 (택1)
1. 정식 설치방법으로 설치 ([jellybean](https://github.com/nanotech/jellybeans.vim#installation) 의 경우)
```shell
mkdir -p ~/.vim/colors
cd ~/.vim/colors
curl -O https://raw.githubusercontent.com/nanotech/jellybeans.vim/master/colors/jellybeans.vim
```
  
2. `~/.vim/colors/` 생성
	- 해당 `컬러스킴.vim`을 다운로드 받아서 해당 디렉토리 생성후 집어넣어줍시다.
	- (colors 가 없는 경우 만들어서 넣어주면 됩니다.)

3. `/usr/share/vim/vim{버전}/colors/` 에 추가
	- 해당 `컬러스킴.vim`을 다운로드 받아서 해당 디렉토리에 집어넣어줍시다. 


#### 참고
- [# vim 에디터 이쁘게 사용하기](https://medium.com/sunhyoups-story/vim-%EC%97%90%EB%94%94%ED%84%B0-%EC%9D%B4%EC%81%98%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-5b6b8d546017)
- [# Vim editor 설치 및 설정](https://velog.io/@jarvis_geun/Vim-editor-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%84%A4%EC%A0%95)
- https://github.com/nanotech/jellybeans.vim
- [[vim] vimrc 설정 (vim 기본 설정)](https://hcnam.tistory.com/14)
