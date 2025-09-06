import datetime
from django.shortcuts import render

def home(request):
    context = {"year": datetime.datetime.now().year}
    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")

def certificates(request):
    return render(request, "home/certificates.html")
