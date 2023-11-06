- [[Windows] Git Bash에 zsh (Oh-my-zsh) 설치해서 꾸미기](https://jizard.tistory.com/445)
- [window에서 Git Bash에 oh my zsh 사용하기](https://velog.io/@ehrbs2021/window%EC%97%90%EC%84%9C-Git-Bash%EC%97%90-oh-my-zsh-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)

#### git bash 실행시 자동으로 zsh 실행되게 하는 코드
```vim
if [ -t 1 ]; then
exec zsh
fi
```