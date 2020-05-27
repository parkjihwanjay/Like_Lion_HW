from django.shortcuts import render, redirect
from .models import Post, Comment
from datetime import date, datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

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

    if request.method == "POST":
        now = datetime.now()
        Comment.objects.create(
            post = post,
            content = request.POST['content'],
            comment_date = (str(now.year)+"년 "+str(now.month)+"월 "+str(now.day)+"일 "+str(now.hour)+"시 "+str(now.minute)+"분"),
            author = request.user
        )
        return redirect('detail', post_pk)

    return render(request, "detail.html", {'post':post})

@login_required(login_url = '/registration/login.html')
def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_post = Post.objects.create(
            title = request.POST["title"],
            content = request.POST["content"],
            day = request.POST["day"],
            time = request.POST["time"],
            author = request.user
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

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request):
    if (request.method =="POST"):
        found_user = User.objects.filter(username=request.POST['username'])
        if(len(found_user)>0):
            error = "username이 이미 존재합니다"
            return render(request, 'registration/signup.html', {'error':error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user,
        backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect('home')

    return render(request, 'registration/signup.html')

def login(request):
    if (request.method == "POST"):
        found_user =auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )

        if(found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error})
    
        auth.login(request, found_user,
                    backend= "django.contrib.auth.backends.ModelBackend")
        return redirect(request.GET.get('next', '/'))

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def mymy(request):
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

    return render(request, 'mymy.html', {'posts':posts, 'remains':remain_times})