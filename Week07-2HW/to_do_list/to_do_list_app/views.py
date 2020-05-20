from django.shortcuts import render, redirect
from .models import Post
from datetime import date

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('day','time')
    remain_times = []
    class remain_time():
        def __init__(self, rd, pk_rt):
            self.pk = int(pk_rt)
            self.remain_time =rd
        def __str__(self):
            return self.remain_time
    for post in posts:
        remain_day = (post.day-date.today()).days
        post_pk=post.pk
        semi_time = remain_time(remain_day, post_pk)
        remain_times.append(semi_time)

    return render(request, 'home.html', {'posts':posts, 'remains':remain_times})

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, "detail.html", {'post':post})

    
def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_post = Post.objects.create(
            title = request.POST["title"],
            content = request.POST["content"],
            day = request.POST["day"],
            time = request.POST["time"]
        )
        return redirect('detail', new_post.pk)

    return render(request, 'new.html')

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            day = request.POST['day'],
            time = request.POST['time']
        )
        return redirect('detail', post_pk)
    return render(request, 'edit.html', {'post':post})

def delete(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.delete()
    return redirect('home')