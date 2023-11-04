#### How to Install oh-my-zsh
```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

#### oh-my-zsh plugin
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

#### fzf
```shell
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf

~/.fzf/install
```