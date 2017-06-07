from blog.models import Blog
from django.shortcuts import get_object_or_404, render


def blog_lists(request):
    "文章列表页"
    blog_lists = Blog.objects.all()
    return render(request, 'blog/list.html', {'blog_lists': blog_lists})


def blog_detail(request, my_args):
    """文章详情页"""
    blog_detail = get_object_or_404(Blog, id=my_args)
    context = {'blog_detail': blog_detail}
    return render(request, 'blog/detail.html', context=context)
