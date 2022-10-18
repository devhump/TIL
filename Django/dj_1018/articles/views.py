from django.shortcuts import redirect, render
from articles.forms import ArticleForm, CommentForm
from .models import Article

# Create your views here.
def index(request):

    articles = Article.objects.order_by("-pk")

    context = {
        "articles": articles,
    }

    return render(request, "articles/index.html", context)


def create(request):

    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }

    return render(request, "articles/form.html", context)


def detail(request, article_pk):

    article = Article.objects.get(pk=article_pk)

    comment_form = CommentForm()

    context = {
        "article": article,
        "comment_form": comment_form,
    }

    return render(request, "articles/detail.html", context)


def comments(request, article_pk):

    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()

    return redirect("articles:detail", article_pk)
