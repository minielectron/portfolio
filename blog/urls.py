from django.urls import path
from . import views

app_name="blog" #Works as namespace

urlpatterns = [
    path('', views.blogs, name="blog"),
    path('<int:blog_id>', views.detail, name="detail")
]