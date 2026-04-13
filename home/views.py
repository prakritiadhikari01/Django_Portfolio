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
def certificates(request):
    certificates = [
        {
            "title": "Hackathon Nova 2025",
            "issuer": "CAPEC × ITEC-PEC",
            "date": "Jan 27-29, 2026",
            "description": "Developed MoodMate, an ethical AI-powered emotional reflection platform.",
            "tags": ["AI", "Hackathon", "Django", "NLP", "Ethical AI", "Teamwork"],
            "image": "certificates/Nova.png"
        },
        {
            "title": "NIC College Ambassador 2025",
            "issuer": "National Innovation Centre",
            "date": "August 9, 2025",
            "description": "Promoted NIC programs, organized events, and engaged peers as a student ambassador.",
            "tags": ["Leadership", "Student Ambassador", "Event Management", "Networking"],
            "image": "certificates/NIC.png",
        },
        {
            "title": "Django",
            "issuer": "Workshop",
            "date": "2025",
            "description": "Built dynamic web applications using Django framework, applying MVC architecture and database integration.",
            "tags": ["Web Development", "Django", "Backend", "Full-Stack"],
            "image": "certificates/Django.png",
        },
        {
            "title": "Nobel Fundamentals Internship Certificate",
            "issuer": "Nobel Fundamentals (International Program)",
            "date": "2025",
            "description": "Completed 90-hour internship focusing on web design, communication, troubleshooting, and leadership skills.",
            "tags": ["Internship", "Leadership", "Web Design", "Communication", "Technical Skills"],
            "image": "certificates/Nobel.png",
        },
        {
            "title": "Flutter Internship",
            "issuer": "Thulo Technology Pvt. Ltd.",
            "date": "2025",
            "description": "Completed internship on Flutter app development, building responsive mobile applications.",
            "tags": ["Flutter", "Mobile Development", "App Development", "Internship"],
            "image": "certificates/Flutter.png",
        },
        {
            "title": "Git & GitHub",
            "issuer": "Workshop",
            "date": "2024",
            "description": "Mastered version control with Git and GitHub, including branching, merging, and collaborative workflows.",
            "tags": ["Version Control", "Git", "Collaboration", "Software Development"],
            "image": "certificates/Git.png",
        },
        {
            "title": "Hackathon Participation (Yantra)",
            "issuer": "Various / Event",
            "date": "2024",
            "description": "Participated in team-based hackathon, developing 'Sajilo Rental' through ideation, prototyping, and collaboration.",
            "tags": ["Hackathon", "Teamwork", "Innovation", "Problem Solving", "Prototyping"],
            "image": "certificates/Hackathon.png",
        },
        {
            "title": "UI Design",
            "issuer": "Workshop",
            "date": "2024",
            "description": "Designed intuitive and user-friendly interfaces with focus on aesthetics, usability, and user experience principles.",
            "tags": ["UI/UX", "Design", "Creativity", "User Experience"],
            "image": "certificates/UI.png",
        },
        {
            "title": "Digital Marketing",
            "issuer": "Workshop",
            "date": "2025",
            "description": "Learned and applied digital marketing strategies including campaigns, SEO, and social media engagement.",
            "tags": ["Digital Marketing", "SEO", "Campaigns", "Social Media", "Marketing"],
            "image": "certificates/Digital_Marketing.png",
        },
        {
            "title": "Effective Leadership",
            "issuer": "Course",
            "date": "2024",
            "description": "Developed leadership and communication skills through practical exercises and teamwork scenarios.",
            "tags": ["Leadership", "Communication", "Teamwork", "Personal Development"],
            "image": "certificates/Effective_Leadership.png",
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