from django.shortcuts import render



def index(request):
    data = {

    }
    return render(request, 'main/index.html', data)

def tools(request):
    return render(request, 'main/tools.html')

def screen(request):
    return render(request, 'main/screen.html')