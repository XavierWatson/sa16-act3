from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
def work(request):
    return render(request, 'pages/work.html')
def about(request):
    return render(request, 'pages/about.html')
def contact(request):
    return render(request, 'pages/contact.html')