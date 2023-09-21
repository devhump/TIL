from datetime import datetime
from django.shortcuts import redirect, render

# from crud.settings import BASE_DIR
from .models import Todo

# Create your views here.
def index(request):
    # print(BASE_DIR)

    todos = Todo.objects.order_by("-priority")

    today = datetime.today().strftime("%Y-%m-%d")
    # print(today)
    context = {
        "todos": todos,
        "today": today,
    }

    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    # context = {
    #     "content": content,
    #     "priority": priority,
    #     "deadline": deadline,
    # }

    # return render(request, "todos/create.html", context)
    return redirect("todos:index")


def delete(request, pk):

    Todo.objects.get(id=pk).delete()

    return redirect("todos:index")


def update(request, pk):

    todo = Todo.objects.get(id=pk)

    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True

    todo.save()

    return redirect("todos:index")
