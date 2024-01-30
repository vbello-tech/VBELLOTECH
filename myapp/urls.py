from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog_list, name="blog_list"),
    path('blog/<int:pk>/', views.blog_detail, name="blog_detail"),
    path('portfolio/', views.projects, name="project"),
    path('contact/', views.contact, name="contact"),
]