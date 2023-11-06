---
title : 
aliases : 
tags : [Django, JumpToDajngo]
---

p115

```django
{% comment %} templates/pybo/question_form.html {% endcomment %}

{% extends 'base.html' %}

{% block content %}
<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>
    <form method="post" class="post-form my-3">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary"> 저장하기</button>
    </form>
</div>
{% endblock content %}
```

![|400](점프%20투%20장고.png)

- 위 코드 처럼 `{{ form.as_p }}` 태그는 form 엘리먼트와 입력 항목을 자동으로 생성해 주어 편리하긴 하나, 부트 스트랩을 적용할 수 없다. 

- 이때, QuestionForm 클래스 내부에 있는 Meta 클래스에 widgets 속성을 추가하면 부트스트랩을 적용할 수 있다. 

```python
from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class' : 'form-control'}),
            'content': forms.Textarea(attrs={'class' : 'form-control', 'rows' : 10}),
        }
```

![](점프%20투%20장고-1.png)

- 또, Label 속성을 지정하여, 기존 폼의 라벨링을 수정할 수도 있다.
![|200](점프%20투%20장고-2.png)

```python
from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class' : 'form-control'}),
            'content': forms.Textarea(attrs={'class' : 'form-control', 'rows' : 10}),
        }
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }
```

- 아니면 위 코드에서 widgets 항목을 삭제하고 수동으로 폼을 작성할 수도 있다.
```django
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>
    <form method="post" class="post-form my-3">
        {% csrf_token %}
        <!-- 오류표시 Start -->
        {% if form.errors %}
        <div class="alert alert-danger" role="alert">
        {% for field in form %}
            {% if field.errors %}
            <strong>{{ field.label }}</strong>
            {{ field.errors }}
            {% endif %}
        {% endfor %}
        </div>
        {% endif %}
        <!-- 오류표시 End -->
        <div class="form-group">
            <label for="subject">제목</label>
            <input type="text" class="form-control" name="subject" id="subject"
                value="{{ form.subject.value|default_if_none:'' }}">
        </div>
        <div class="form-group">
            <label for="content">내용</label>
            <textarea class="form-control" name="content"
                id="content" rows="10">{{ form.content.value|default_if_none:'' }}</textarea>
        </div>
        <button type="submit" class="btn btn-primary"> 저장하기</button>
    </form>
</div>
{% endblock content %}

```

- `value="{{ form.subject.value|default_if_none:'' }}">`  이 코드는 오류 발생 시 기존 입력 값을 유지하기 위해 삽입됐다. 파이프 라인(`|`) 오른쪽 코드는 공란일 경우, `none`이 표시되는데, 대신 공란을 나타내기 위한 것이다. 

![](점프%20투%20장고-3.png)


- navbar의 경우, base 파일에 삽입해도 되지만, 따로 만들어서 include를 사용 해도 된다. ("navbar.html" 파일 따로 생성)
	- 이와 같은 경우 중복되는 코드를 줄일 뿐만 아니라, 특정 기능이나 레이아웃의 유지/보수 면에서 유리하다

```django 
{% include "navbar.html" %}
```


- 페이징 연습을 위한 더미 게시글 작성
```shell
from pybo.models import Question
from django.utils import timezone
for i in range(300):
	q = Question(subject="테스트 데이터입니다:[%03d]" % i, content="내용무", create_date=timezone.now())
	q.save()
```

![](점프%20투%20장고-4.png)


```python
from django.core.paginator import Paginator

def index(request):
    """
    pybo 목록 출력
    """
    page = request.GET.get('page', '1') # 페이지

    question_list = Question.objects.order_by('-create_date')
    
    paginator = Paginator(question_list, 10) # 한 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {
        "question_list" : page_obj,
    }
    return render(request, 'pybo/question_list.html', context)
```

- 👉 장고 **Paginator 클래스**를 활용한 페이징 처리
![](점프%20투%20장고-5.png)

- 설정값 처럼 페이지당 10개의 게시물씩 출력되는 걸 확인할 수 있다. 
- 여기에 질문 목록 리스트 템플릿에 페이징 처리를 하면 아래와 같이 페이지 네비게이션 버튼이 생성된다.

```django
<!-- 페이징처리 시작 -->
     <ul class="pagination justify-content-center">
        <!-- 이전페이지 -->
        {% if question_list.has_previous %}
        <li class="page-item">
            <a class="page-link" href="?page={{ question_list.previous_page_number }}">이전</a>
        </li>
        {% else %}
        <li class="page-item disabled">
            <a class="page-link" tabindex="-1" aria-disabled="true" href="#">이전</a>
        </li>
        {% endif %}
        <!-- 페이지리스트 -->
        {% for page_number in question_list.paginator.page_range %}
        {% if page_number >= question_list.number|add:-5 and page_number <= question_list.number|add:5 %}
            {% if page_number == question_list.number %}
            <li class="page-item active" aria-current="page">
                <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
            </li>
            {% else %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
            </li>
            {% endif %}
        {% endif %}
        {% endfor %}
        <!-- 다음페이지 -->
        {% if question_list.has_next %}
        <li class="page-item">
            <a class="page-link" href="?page={{ question_list.next_page_number }}">다음</a>
        </li>
        {% else %}
        <li class="page-item disabled">
            <a class="page-link" tabindex="-1" aria-disabled="true" href="#">다음</a>
        </li>
        {% endif %}
    </ul>
    <!-- 페이징처리 끝 -->
```

![](점프%20투%20장고-7.png)

- 지나치게 페이지 네비게이션이 많으니 조절하는 코드 삽입 후의 모습
```django
    {% if page_number >= question_list.number|add:-5 and page_number <= question_list.number|add:5 %}
	...
	{% endif %}
```
- (현재 페이지 기준 좌우로 5개씩만 노출 되도록 설정해 주는 코드이다)
![](점프%20투%20장고-8.png)


![](점프%20투%20장고-6.png)


### 템플릿 필터 만들기
- 앱 내에 `templatetags` 라는 디렉터리를 만든다.
- 해당 위치에 `pybo_filter.py` 라는 파일을 만든다.
```python
# mysite/pybo/templatetags/pybo_filter.py

from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg
```

- sub 함수에 애너테이션을 적용하면, ==템플릿에서 해당 함수를 필터로 사용할 수 있다. ==

#### 템플릿 필터 사용하기
```django
{% load pybo_filter %}

{{ question_list.paginator.count|sub:question_list.start_index|sub:forloop.counter0|add:1}}
<!-- 전체 게시물 개수 - 시작인덱스 - 현재인덱스 + 1 -->
```
- 템플릿 파일 최상단(extend 문이 있으면 그 아래)에 위치한다. 


### 게시물 답변 개수 출력하기
```django
<a href="{% url 'pybo:detail' question.id %}">
	{{question.subject}}
	{% if question.answer_set.count > 0 %}
	<span class="text-danger small ml-2">
		{{question.answer_set.count}}
	</span>
	{% endif %}
</a>
```

![](점프%20투%20장고-9.png)


#### 페이지 전환 후 작업중이던 섹션(위치)으로 이동하기
- 현재까지는 댓글에 추가/삭제 후에 자동적으로 페이지 가장 상단으로 이동하지만, 이 페이지 전환 후에 다시 내가 보고 있던 부분으로(작업중이던) 이동시키는 방법을 의미한다. 

- 기존 댓글
```django
<a name="answer_{{ answer.id }}"></a>
```


```python
# 기존 answer_create URL
return redirect('pybo:detail', question_id=question.id)

# 변경후 answer_create URL
return redirect('{}#anwer_{}'.format(resolve_url('pybo:detail', question_id=question.id), answer.id))

```



#### 게시판에 마크다운 기능 추가하기
- 패키지 설치하기
```shell
pip install markdown
```

- 마크다운 필터 등록 
```python
# mysite/pybo/templatetags/pybo_filter.py

from django import template
import markdown # 추가
from django.utils.safestring import mark_safe # 추가

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter()
def mark(value):

    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))
```

- 템플릿에 적용하기
```django
<div> {{ question|mark}} </div>
```

![](점프%20투%20장고-10.png)

### 검색 기능 추가하기
```python
from django.db.models import Q

kw = request.GET.get('kw', '') # 검색어

if kw:
	question_list = question_list.filter(
		Q(subject__icontains=kw) |                # 제목검색
		Q(content__icontains=kw) |                # 내용 검색
		Q(author__username__icontains=kw) |       # 질문 글쓴이 검색
		Q(answer__author__username__icontains=kw) # 답글 글쓴이 검색
	).distinct()
```

- Q 함수는 OR 조건으로 데이터를 조회하는 장고의 함수
- `filter`함수 뒤의 `distint`는 조회결과의 중복을 제거하는 역할

#### 검색 기능을 GET 방식으로 구현하는 이유
- 웹 브라우저에서 입력한 URL
```shell
localhost:8000/?kw=파이썬&page=1
```

- kw 값을 얻기 위한 코드 예
```python
kw = request.GET.get('kw', '') # 검색어
```

- GET 방식을 이용하면 URL에 파라미터 값으로 인자(검색어)를 전달하며, 이를 확인하여 검색 기능을 수행한다. 
- 그러나 POST 방식으로 전달할 경우, page 역시 POST 방식으로 전달 해야하며, POST 방식으로 검색, 페이징 기능을 만들게 되면 '새로고침'이나 ' 뒤로가기' 를 했을 때, '만료된 페이지' 오류를 종종 만나게 된다. **이는, POST 방식은 동일한 POST 요청이 발생할 경우 중복을 방지하기 위해 오류를 발생 시키기 때문이다.**


### 정렬 기능 추가하기
- question_list.html
```django
<div class="col-2">
	<select class="form-control so">
		<option value="recent" {% if so == 'recent' %}selected{% endif %}>최신순</option>
		<option value="recommend" {% if so == 'recommend' %}selected{% endif %}>추천순</option>
		<option value="popular" {% if so == 'popular' %}selected{% endif %}>인기순</option>
	</select>
</div>

...

<form id="searchForm" method="get" action="{% url 'index' %}">
	<input type="hidden" id="kw" name="kw" value="{{ kw|default_if_none:'' }}">
	<input type="hidden" id="page" name="page" value="{{ page }}">
	<input type="hidden" id="so" name="so" value="{{ so }}"> # 추가
</form>

...

```

```js
    $(".so").on('change', function() {
        $("#so").val($(this).val());
        $("#page").val(1);
        $("#searchForm").submit();
    });
```


```python
from django.db.models import Q, Count

    
def index(request):
	...
	
    # 정렬 (조회)
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')
    ...
```


- 코드 변경 내역 확인
```shell
git diff
```
- 👉 해당 명령어 사용시 `-`표시되는 부분이 삭제, `+` 부분이 추가되는 내용이다!

- 한글이 깨질 때
```shell
set LC_ALL=C.UTF-8

# 한글이 깨질 때 (window powershell 의 경우)
$Env:LC_ALL = "C-UTF-8"
```

- 코드의 변경 내역 되돌리기
```shell
git restore 파일명
```

- git commit -a
```shell
git commit -a -m "커밋메시지"
```
- `-a` 옵션은 커밋할 때 add 명령도 함께 처리하라는 옵션이다.


- `cat mysite.log` 명령에서 사용된 `cat` 명령은 파일 내용 전체를 출력하는 유닉스 명령이다. 보통 로그를 확인할 때는 `cat` 보다는 `tail -f mysite.log`를 주로 사용한다.  `tail -f mysite.log`를 실행하면 mysite.log 파일에 로그가 쌓일 때마다 로그의 내용이 자동으로 출력된다.
