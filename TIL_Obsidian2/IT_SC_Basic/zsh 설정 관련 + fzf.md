---
tags:
  - Linux
  - HomeServer
---

- [Ubuntu에 Oh My Zsh 설치](https://log4cat.tistory.com/7)

#### zsh 설치
```shell
sudo apt-get install zsh -y
```
#### How to Install oh-my-zsh
```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### agnoster theme font
```shell
sudo apt-get install fonts-powerline -y
```
#### oh-my-zsh plugin
```shell

cd #home으로 이동후
vim .zshrc
```

```shell
plugins(
	git
	sudo
	colored-man-pages
	zsh-syntax-highlighting
	zsh-autosuggestions
)
```

```shell
# oh-my-zsh

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

```shell
source .zshrc
```

##### oh-my-zsh theme
- C
- [x] candy
- [x] **crcandy**

- D
- [x] **dallas**
- [x] **dieter**

- others
- [x] **fino-time 🌟**
- [x] mikeh

- [x] jtriley
- [x] rkj-repos
- [x] xiong-chiamiov-plus


#### fzf
```shell
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf

~/.fzf/install
```
