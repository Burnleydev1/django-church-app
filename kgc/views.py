from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'kgc/index.html', {'title': 'Kgc-home'})

def about(request):
    return render(request, 'kgc/about.html', {'title': 'kgc-about'})
    
def ministries(request):
    return render(request, 'kgc/ministries.html', {'title': 'kgc-ministries'})

def team(request):
    return render(request, 'kgc/board.html', {'title': 'kgc-team'})

def gallery(request):
    return render(request, 'kgc/gallery.html', {'title': 'kgc-gallery'})

def praise_and_worship(request):
    return render(request, 'kgc/praise-and-worship.html', {'title': 'kgc-praise_and_worship'})

def children(request):
    return render(request, 'kgc/children.html', {'title':'kgc-children-ministry'})

def women_ministry(request):
    return render(request, 'kgc/women-min.html', {'tile': 'kgc-women_ministry'})

def youths(request):
    return render(request, 'kgc/youth.html', {'title': 'kgc-youth'})

def men_ministry(request):
    return render(request, 'kgc/men-min.html', {'title': 'kgc-men_ministry'})

def intercessory(request):
    return render(request, 'kgc/intercessory.html', {'title': 'kgc-intercessory'})

def sermons(request):
    return render(request, 'kgc/sermons.html', {'title': 'kgc-sermons'})
