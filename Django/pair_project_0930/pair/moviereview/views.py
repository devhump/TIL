from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Review

# Create your views here.
def index(request):

    reviews = Review.objects.all()

    context = {"reviews": reviews}

    return render(request, "moviereview/index.html", context)


def new(request):

    return render(request, "moviereview/new.html")


def create(request):

    title = request.GET.get("title_")
    content = request.GET.get("content_")

    Review.objects.create(title=title, content=content)

    return redirect("index")

def detail(request, pk):
    review = Review.objects.get(id=pk)

    context = {
        'review': review,
    }

    return render(request, "moviereview/detail.html", context)

def edit(request, pk_):
    review = Review.objects.get(pk=pk_)

    context = {
        'review': review,
    }

    return render(request, "moviereview/edit.html", context)

def update(request, pk):
    review = Review.objects.get(pk=pk)

    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.save()

    return redirect('index')

def delete(requst, pk):
    Review.objects.get(pk=pk).delete()

    return redirect('index')
