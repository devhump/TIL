---
tags:
  - rasberrypi
---
### initial installation
```shell
sudo apt update && sudo apt upgrade -y

sudo apt-get install zsh vim iptables -y

sudo apt-get install dstat htop btop iftop neofetch -y

sudo apt-get install tldr exa duf nnn mc -y

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