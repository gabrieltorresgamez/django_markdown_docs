from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:link>", views.render_markdown, name="render_markdown"),
]
