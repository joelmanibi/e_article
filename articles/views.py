from django.shortcuts import render
from .models import articles
from django.contrib import messages

# Create your views here.

def index (request):
    art = articles.objects.all()
    return render(request, 'articles/index.html',{'art':art})

def enregistrement (request):
    if request.method=="POST":
        a_nom = request.POST['nom-articles']
        b_num = request.POST['Batch-number']
        a_com = request.POST['com-articles']
        img_a = request.POST['img-articles']
        articles.objects.create(nom_article=a_nom,batch_number=b_num,commentaire=a_com,image=img_a)

    articls = articles.objects.all()
    return render(request,'articles/enregistement.html',{'articls':articls})