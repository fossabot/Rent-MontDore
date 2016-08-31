from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'presentation/home.html', locals())

def description(request):
    return render(request, 'presentation/description.html', locals())
