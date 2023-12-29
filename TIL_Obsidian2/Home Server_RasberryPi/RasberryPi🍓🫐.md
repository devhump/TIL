---
tags:
  - rasberrypi
  - HomeServer
---

#### at the begining
```shell
sudo apt update && sudo apt upgrade -y
```

### initial installation
```shell
sudo apt-get install zsh vim iptables -y

sudo apt-get install dstat htop btop iftop neofetch -y

sudo apt-get install tldr exa duf nnn mc -y

```

##### iftop
```shell
sudo iftop -h

sudo iftop
```


### 로케일(locale) 변경 시 한글 깨질 때
```shell
# 폰트 설치
sudo apt install fonts-nanum fonts-nanum-extra
sudo apt-get install fonts-powerline

# 입력기 설치
sudo apt install nabi

sudo apt install im-config
```



#### Powerline fonts Quick installation
- [Powerline fonts (github)](https://github.com/powerline/fonts#powerline-fonts)
#### method #1
```shell
sudo apt-get install fonts-powerline
```

#### method #2
```shell
# clone
git clone https://github.com/powerline/fonts.git --depth=1
# install
cd fonts
./install.sh
# clean-up a bit
cd ..
rm -rf fonts
```

### Next Step
- [[vim 설정]]
- [[zsh 설정 관련 + fzf]]
- [[Home-server - 원격관리 & 보안]]
	- [라즈베리파이 - fail2ban 오류 해결](https://biology-statistics-programming.tistory.com/188)