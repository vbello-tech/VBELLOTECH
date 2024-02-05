from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog_list, name="blog_list"),
    path('blog/<int:pk>/', views.blog_detail, name="blog_detail"),
    path('portfolio/', views.projects, name="project"),
    path('contact/', views.contact, name="contact"),
    path('login/', LoginView.as_view(
        template_name='login.html',
        success_url=reverse_lazy('home')
    ), name="login"),
    path('add-project/', views.add_project, name="add_project"),
]