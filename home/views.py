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

from django.shortcuts import render

def certificates_view(request):
    certificates = [
        {
            "title": "NIC College Ambassador 2025",
            "issuer": "NIC",
            "date": "August 9, 2025",
            "description": "National Innovation Certificate.",
            "tags": ["Networking", "Certificate"],
            "image": "/static/images/NIC.png",
            "link": "https://github.com/prakritiadhikari01/Certificates/blob/main/NIC.pdf"
        },
        {
            "title": "Django",
            "issuer": "Course/Workshop",
            "date": "2023",
            "description": "Web development using Django framework.",
            "tags": ["Web Development", "Django"],
            "image": "/static/images/Django.png",
            "link": "https://github.com/prakritiadhikari01/Certificates/blob/main/Django.pdf"
        },
        {
            "title": "Nobel Certificate",
            "issuer": "Institution",
            "date": "2023",
            "description": "Recognition certificate.",
            "tags": ["Recognition"],
            "image": "/static/images/Nobel.png",
            "link": "https://github.com/prakritiadhikari01/Certificates/blob/main/Nobel.pdf"
        },
        {
            "title": "Git & GitHub",
            "issuer": "Course/Workshop",
            "date": "2023",
            "description": "Version control using Git & GitHub.",
            "tags": ["Version Control", "Git"],
            "image": "/static/images/Git.png",
            "link": "https://github.com/prakritiadhikari01/Certificates/blob/main/Git.pdf"
        },
        {
            "title": "Hackathon Participation",
            "issuer": "Various / Event",
            "date": "Feb 2024",
            "description": "Team-based hackathon participation showcasing ideation and prototyping.",
            "tags": ["Hackathon", "Teamwork", "Prototype"],
            "image": "/static/images/Hackathon.png",
            "link": "https://github.com/prakritiadhikari01/Certificates/blob/main/Hackathon.pdf"
        },
        {
            "title": "UI Design",
            "issuer": "Workshop",
            "date": "2023",
            "description": "Designing user-friendly interfaces and experiences.",
            "tags": ["UI/UX", "Design"],
            "image": "/static/images/UI.png",
            "link": "https://github.com/prakritiadhikari01/Certificates/blob/main/UI.pdf"
        },
        {
            "title": "Digital Marketing",
            "issuer": "Workshop",
            "date": "2023",
            "description": "Digital marketing strategies and campaign execution.",
            "tags": ["Marketing", "Digital"],
            "image": "/static/images/Digital_Marketing.png",
            "link": "https://github.com/prakritiadhikari01/Certificates/blob/main/Digital_Marketing_Workshop.pdf"
        },
        {
            "title": "Effective Leadership",
            "issuer": "Workshop",
            "date": "Mar 2024",
            "description": "Workshop on leadership and communication skills.",
            "tags": ["Leadership", "Communication"],
            "image": "/static/images/Effective_Leadership.png",
            "link": "https://github.com/prakritiadhikari01/Certificates/blob/main/Effective_Leadership.pdf"
        },
    ]
    return render(request, "home/certificates.html", {"certificates": certificates})


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