from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'general/index.html')

def about(request):
    return render(request, 'general/about.html')

def service(request):
    return render(request, 'general/services.html')

def project(request):
    return render(request, 'general/projects.html')

def blog(request):
    return render(request, 'general/blog.html')

def contact(request):
    return render(request, 'general/contact.html')