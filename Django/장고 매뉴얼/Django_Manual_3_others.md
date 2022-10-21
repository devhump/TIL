## 1. (1:N) 관계 설정

- [pdf : django_13](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1c0524e1-fb57-41e1-8244-e926e5fc4c1f/django_13.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221020T155748Z&X-Amz-Expires=86400&X-Amz-Signature=bd2ae123ccdf7a1219c146d1e25ede03fa89a28f5bc24f570f2f2cdfd3350acb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22django_13.pdf%22&x-id=GetObject)

### 1-1. 외래키(FK) 설정

- models

```python
# articles/models.py

# case 1. FK 가 하나일 때 
class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	content = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
		return self.content

# case 2. FK 가 둘 이상일 때
class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자) 으로 작성하는 것을 권장 (`article`, `user` 등)

- forms

```python
# articles/forms.py

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ('article', 'user',)
```



### 1-2. 작성자 확인

```python
# articles/views.py
def comments_delete(request, article_pk, comment_pk):
	comment = Comment.objects.get(pk=comment_pk)
	if request.user == comment.user: # 로그인한 유저가 작성자와 같은지
		comment.delete()
		return redirect('articles:detail', article_pk)
```



- templates

```django
<!-- articles/detail.html -->
{% extends 'base.html' %}
{% block content %}
	...
	<ul>
        {% for comment in comments %}
		<li>
		{{ comment.user }} - {{ comment.content }}
		{% if request.user == comment.user %}
			<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
				{% csrf_token %}
				<input type="submit" value="DELETE">
			</form>
		{% endif %}
```



### 1-3. 생성 (저장)

```python
# articles/views.py

def comments_create(request, pk):
	article = Article.objects.get(pk=pk)
	comment_form = CommentForm(request.POST)
	if comment_form.is_valid():
		comment = comment_form.save(commit=False) #save 중지
		comment.article = article # FK에 객체값 삽입
		comment.save()
		return redirect('articles:detail', article.pk)
```



### 1-4. READ

```python
# articles/views.py
from .models import Article, Comment

def detail(request, pk):
	article = Article.objects.get(pk=pk)
	comment_form = CommentForm()
	comments = article.comment_set.all() #context 바로 넘겨주기 가능
	context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
        #'comments': article.comment_set.all(),
        }

    return render(request, 'articles/detail.html', context)
```



```django
<!-- articles/detail.html -->
{% extends 'base.html' %}
{% block content %}
...
<a href="{% url 'articles:index' %}">back</a>
<hr>
<h4>댓글 목록</h4>
<ul>
    {% for comment in comments %}
    <li>{{ comment.content }}</li>
    {% endfor %}
</ul>
<hr>
...
{% endblock content %}
```



### 1-5. 삭제

- urls & views

```py
# articles/urls.py
urlpatterns = [
	...,
	path('<int:article_pk>/comments/<int:comment_pk>/delete/', 	views.comments_delete, name='comments_delete'),
]


# articles/views.py
def comments_delete(request, article_pk, comment_pk):
	comment = Comment.objects.get(pk=comment_pk)
	comment.delete()
	return redirect('articles:detail', article_pk)
```



- templates

```html
<!-- articles/detail.html -->
{% block content %}
...
<h4>댓글 목록</h4>
    <ul>
    {% for comment in comments %}
        <li>
        {{ comment.content }}
            <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
        </form>
        </li>
    {% endfor %}
    </ul>
<hr>
...
{% endblock content %}
```



### 1-6. 댓글 개수 출력

```django
• DTL filter - length 사용
{{ comments|length }}
{{ article.comment_set.all|length }}

• Queryset API - count() 사용
{{ comments.count }}
{{ article.comment_set.count }}

```



- template

```django
<!-- articles/detail.html -->
<h4>댓글 목록</h4>
{% if comments %}
	<p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
{% endif %}
```



### 1-7. DTL for empty

```html
<!-- articles/detail.html -->

{% for comment in comments %}
    <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
        </form>
	</li>
	{% empty %}
	<p>댓글이 없어요..</p>
{% endfor %}
```



## 2. 이미지 설정

- [pdf : django_12](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/65750eab-26e7-441b-8a0e-a549aad431b0/django_12.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221020T162336Z&X-Amz-Expires=86400&X-Amz-Signature=ba1e1c516bd9ddd664e76e6f41e16742cf01105e472ca8eae5c20201da1b0c69&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22django_12.pdf%22&x-id=GetObject)





```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #추가
from django.conf import settings #추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include("articles.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 마지막 부분 추가
```

