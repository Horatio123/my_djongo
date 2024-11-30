from django.urls import path

from . import views

urlpatterns = [
    path("getCommitList", views.index, name="index"),
    path("getDiffList", views.index2, name="index2"),

]
