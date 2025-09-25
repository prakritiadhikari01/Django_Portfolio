import datetime
from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    context = {"year": datetime.datetime.now().year}
    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")

def projects(request):
    return render(request, 'home/projects.html')

def certificates(request):
    return render(request, "home/certificates.html")

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves to database
            success = True
            form = ContactForm()  # clear the form
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form, 'success': success})