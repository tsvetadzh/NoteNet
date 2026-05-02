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

def class_eight(request):
    return render(request, 'classes/eight.html')

def class_nine(request):
    return render(request, 'classes/nine.html')

def class_ten(request):
    return render(request, 'classes/ten.html')

def class_eleven(request):
    return render(request, 'classes/eleven.html')

def class_twelve(request):
    return render(request, 'classes/twelve.html')

def eight_system(request):
    return render(request, 'subjects/eight_system.html')

def eight_ai(request):
    return render(request, 'subjects/eight_ai.html')

def eight_networks(request):
    return render(request, 'subjects/eight_networks.html')

# Subject pages - Grade 9
def nine_system(request):
    return render(request, 'subjects/nine_system.html')

def nine_networks(request):
    return render(request, 'subjects/nine_networks.html')

def ten_system(request):
    return render(request, 'subjects/ten_system.html')

def ten_networks(request):
    return render(request, 'subjects/ten_networks.html')

def eleven_system(request):
    return render(request, 'subjects/eleven_system.html')

def eleven_networks(request):
    return render(request, 'subjects/eleven_networks.html')

def twelve_system(request):
    return render(request, 'subjects/twelve_system.html')

def twelve_networks(request):
    return render(request, 'subjects/twelve_networks.html')