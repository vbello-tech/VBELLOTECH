from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.urls import reverse


# Create your views here.

def home(request):
    projects = Project.objects.order_by('-published_date')
    context = {
        'projects': projects
    }
    return render(request, 'home.html', context)


def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid:
            portfolio = form.save(commit=False)
            portfolio.save()
            return redirect('/')
        form = ProjectForm()
    else:
        form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, "add_project.html", context)


# defining function to display all the blog post.
def blog_list(request):
    all_post = Blog.objects.order_by("-publish_date")

    context = {
        'all_post': all_post
    }

    return render(request, "myapp/blog_list.html", context)


def blog_detail(request, pk):
    detail = Blog.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = detail
            comment.save()
            return redirect('blog_detail', pk=detail.pk)
        form = CommentForm()
    else:
        form = CommentForm()

    context = {
        'detail': detail,
        'form': form
    }

    return render(request, "myapp/blog_detail.html", context)


def projects(request):
    projects = Project.objects.order_by('-published_date')
    context = {
        'projects': projects
    }
    return render(request, 'myapp/portfolio.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # print(name, email, message)
        send_mail(
            name,
            message,
            email,
            ['vbellotech@gmail.com'],
            fail_silently=False,
        )

        return redirect('home')
    else:
        return redirect('home')


def handler404(request, exception):
    context = {"<h1>PAGE NOT FOUND!! ARE YOU SURE YOU ARE NAVIGATING TO THE RIGHT PAGE?</h1>"}
    response = render(request, "404.html", context)
    response.status_code = 404
    return response


def handler500(request):
    context = {"<h1>OOPS !!! <br> SEVER ERROR!!! <br> </h1>"}
    response = render(request, "500.html", context)
    response.status_code = 500
    return response
