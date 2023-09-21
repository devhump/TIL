from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):

    articles = Article.objects.all()

    context = {
        "articles": articles,
    }

    return render(request, "app1004/index.html", context)


# def new(request):
#     article_form = ArticleForm()
#     context = {
#         "article_form": article_form,
#     }

#     return render(request, "app1004/new.html", context=context)


def create(request):
    if request.method == "POST":
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # Article.objects.create(title=title, content=content)

        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("app1004:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }

    return render(request, "app1004/new.html", context=context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        "article": article,
    }

    return render(request, "app1004/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:datail", article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }

    return render(request, "app1004/update.html", context)
