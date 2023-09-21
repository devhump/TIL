from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:article_pk>", views.detail, name="detail"),
    path("<int:article_pk>/comments/", views.comments, name="comments"),
]
