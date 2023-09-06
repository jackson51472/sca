from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("index.html", views.IndexView.as_view(), name="index"),
    path("contatos.html", views.ContatoView.as_view(), name="index"),
]