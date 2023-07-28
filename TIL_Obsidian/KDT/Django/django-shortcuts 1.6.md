---
title : 
aliases : []
tags : [Django]
---

#### 개요
- 장고를 사용하면서 `python manage.py ~~`  라는 명령어를 굉장히 많이 쓰게 된다. 
- 이 패키지를 설치하면, 해당 명령어를 단축어를 통해 사용할 수 있게 해준다.
- [pypi.org - django-shortcuts 1.6](https://pypi.org/project/django-shortcuts/)

![](assets/django-shortcuts%201.6.png)

> "You spend too much time typing `python manage.py`"

#### How to Install and use?
```shell
# install
pip install django-shortcuts

# Usage
$ django <command or shortcut>

$ cd any/project/subdirectory
$ django <command or shortcut>
```

- 나도 아직 다양하게는 안 써봤지만, 'mm' 이랑 'm'은 유용하게 사용중이다.
	- `python manage.py makemigrations` 👉 `django mm`
	- `python manage.py migrate` 👉 `django m`


#### shortcuts
```plain
# Django
'c'  : 'collectstatic',
'r'  : 'runserver',
'sd' : 'syncdb',
'sp' : 'startproject',
'sa' : 'startapp',
't'  : 'test',

# Shell
'd'  : 'dbshell',
's'  : 'shell',

# Auth
'csu': 'createsuperuser',
'cpw': 'changepassword',

# South
'm'  : 'migrate',
'mm' : 'makemigrations',
'sm' : 'schemamigration',
'dm' : 'datamigration',

# Haystack
'ix' : 'update_index',
'rix': 'rebuild_index',

# Django Extensions
'sk' : 'generate_secret_key',
'rdb': 'reset_db',
'rp' : 'runserver_plus',
'shp': 'shell_plus',
'url': 'show_urls',
'gm' : 'graph_models',
'rs' : 'runscript'
```