from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


#defining function to display all the blog post.
def blog_list(request):
    all_post = Blog.objects.order_by("-publish_date")

    context = {
        'all_post':all_post
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
        'detail':detail,
        'form':form
    }

    return render(request, "myapp/blog_detail.html", context)

def projects(request):
    projects = Project.objects.order_by('-published_date')
    context = {
        'projects': projects
    }
    return render(request, 'myapp/portfolio.html', context)


