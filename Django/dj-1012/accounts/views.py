from django.contrib.auth import login as auth_login #추가
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):

    return render(request, 'accounts/index.html')


def signup(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup.html', context)


def detail(request):

    users = get_user_model().objects.all()

    context = {
        'users' : users,
    }

    return render(request, 'accounts/detail.html', context)


def profile(request, user_pk):

    user = get_user_model().objects.get(pk=user_pk)

    context = {
        'user' : user,
    }

    return render(request, 'accounts/profile.html', context)


def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)