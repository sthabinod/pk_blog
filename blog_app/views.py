from django.shortcuts import render
from .models import BlogTable
from django.contrib.auth.decorators import login_required
# class based views 
# function based views


@login_required
def show_blog(request):
    # list all blogs
    list_blogs = BlogTable.objects.all()
    
    return render(request,"show_blog.html",{'blogs':list_blogs})

@login_required
def create_blog(request):
    return render(request,"create_blog.html")