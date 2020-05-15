from django.shortcuts import render, redirect
from .models import Article
import datetime

# Create your views here.
def index_func(request):
    articles = Article.objects.all()
    
    numofdrama = 0
    numofentertain = 0
    numofmovie = 0

    for component in articles:
        if component.category == "movie":
            numofmovie +=1
        elif component.category == "entertain":
            numofentertain +=1
        elif component.category == "drama":
            numofdrama +=1

    return render(request, 'index.html',{
        'numberofentertain' : numofentertain,
        'numberofdrama' : numofdrama,
        'numberofmovie' : numofmovie 
    })

def detail_func(request, pk_clicked_article):
    article = Article.objects.get(pk=pk_clicked_article)
    return render(request, 'detail.html', {'article_in_html':article})

def drama_func(request):
    semi_article = Article.objects.all()
    articles = []
    for component in semi_article:
        if component.category == "drama":
            articles.append(component)
    return render(request, 'drama.html',{
        "drama_in_html": articles
    })

def entertain_func(request):
    semi_article = Article.objects.all()
    articles = []
    for component in semi_article:
        if component.category == "entertain":
            articles.append(component)

    return render(request, 'entertain.html',{
        "entertain_in_html": articles
    })

def movie_func(request):
    semi_article = Article.objects.all()
    articles = []
    for component in semi_article:
        if component.category == "movie":
            articles.append(component)

    return render(request, 'movie.html',{
        "movie_in_html": articles
    })

def new_func(request):
    if request.method =="POST":
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST["title"],
            content = request.POST["content"],
            category = request.POST["category"],
            time = datetime.datetime.now()
        )
        return redirect('detail_in_html', pk_clicked_article = new_article.pk)
    else:
        return render(request, 'new.html') 