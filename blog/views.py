from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
# Create your views here.

def post_list(request):
    p#osts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html',{'posts':posts})
    return HttpResponse('posts")