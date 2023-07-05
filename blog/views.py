from django.shortcuts import render
from django.shortcuts import get_object_or_404

from blog.models import Post
from django.http import HttpResponseServerError


# Create your views here.


def post_list(request):
    posts_published = Post.objects.filter(status='published')

    context = {'posts_published': list(posts_published)}
    render(request, 'list.html', context=context)


def post_detail(request, post_id):
    try:
        example_obj = get_object_or_404(Post, post_id=post_id)
    except Post.DoesNotExist:
        return HttpResponseServerError('not found')

    context = {'': ''}
    render(request, 'detail.html', context=context)
