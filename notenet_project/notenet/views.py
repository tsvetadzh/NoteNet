from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def addnote(request):
    return render(request, 'addnote.html')

def materials(request):
    return render(request, 'materials.html')

def myclass(request):
    return render(request, 'myclass.html')

def profile(request):
    return render(request, 'profile.html')