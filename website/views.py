from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'website/home.html')
    #return HttpResponse("Welcome to KechGraphix!")


def gallery(request):
    return render(request, 'website/gallery.html')

def about(request):
    return render(request, 'website/about.html')