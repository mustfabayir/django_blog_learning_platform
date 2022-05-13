from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category

# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, 'blog/index.html', context)

def blogs(request):
    context = {
        "blogs": Blog.objects.all(),
        "categories": Category.objects.all()
    }
    return render(request, 'blog/blogs.html', context)

def blog_details(request, slug):
    # blogs = data["blogs"]
    # selected_blog = None

    # for blog in blogs:
    #     if blog["id"] == id:
    #         selected_blog = blog
            
    # blogs  = data["blogs"]
    # selected_blog = [blog for blog in blogs if blog["id"] == id][0]

    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blog-details.html', {'blog': blog})


def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.all(),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, 'blog/blogs.html', context)