from django.urls import path
from core import views

urlpatterns = [
    path("hello/", views.Hello.as_view()),
]
