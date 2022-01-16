from django.shortcuts import render

from lojinha.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'Layout.html', {'posts':posts})
    
def post(request , post_id):
    post = Post.objects.get(pk= post_id)
    return render(request, 'Layout.html', {'posts':post})