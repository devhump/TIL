---
tags:
  - Linux
---

#### How to Install oh-my-zsh
```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### agnoster theme font
```shell
sudo apt-get install fonts-powerline
```
#### oh-my-zsh plugin
```shell
vim .zshrc
```

```shell
plugin(
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
- [x] crunch

- D
- [ ] dallas
- [ ] dieter

- others
- [ ] fino-time
- [ ] mikeh
- [ ] jonathan

- [x] jtriley
- [ ] rkj-repos
- [x] xiong-chiamiov-plus


#### fzf
```shell
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf

~/.fzf/install
```
