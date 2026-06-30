from django.shortcuts import render
from .models import Principal, HeroSlide
from django.contrib import messages
from .models import ContactMessage
from django.shortcuts import render, redirect
def home(request):
    principal = Principal.objects.first()
    hero_slides = HeroSlide.objects.filter(is_active=True)

    context = {
        "principal": principal,
        "hero_slides": hero_slides,
    }

    return render(request, "home.html", context)


def history(request):
    return render(request, "about/history.html")


def vision(request):
    return render(request, "about/vision.html")


def principal_page(request):

    principal = Principal.objects.first()

    context = {
        "principal": principal,
    }

    return render(request, "about/principal.html", context)


def facilities(request):
    return render(request, "about/facilities.html")
def intermediate(request):
    return render(request, "academics/intermediate.html")


def adp(request):
    return render(request, "academics/adp.html")


def bs(request):
    return render(request, "academics/bs.html")


def departments_page(request):
    return render(request, "academics/departments.html")
def faculty(request):
    return render(request, "faculty/index.html")
def downloads(request):
    return render(request, "downloads/index.html")
def gallery(request):
    return render(request, "gallery/index.html")

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        messages.success(
            request,
            "Your message has been submitted successfully."
        )

        return redirect("contact")

    return render(request, "contact/index.html")
def notices(request):
    return render(request, "notices/index.html")


def academic_calendar(request):
    return render(request, "downloads/academic_calendar.html")

def department_detail(request, slug):

    departments = {
        "computer-science": {
            "icon": "💻",
            "name": "Computer Science",
            "description": "The Computer Science Department focuses on programming, software development, databases, web technologies, networking and modern IT skills.",
            "features": ["Programming", "Web Development", "Database Systems", "Networking"],
        },
        "physics": {
            "icon": "⚛️",
            "name": "Physics",
            "description": "The Physics Department provides strong theoretical and practical knowledge through experiments, mechanics, electronics and modern physics.",
            "features": ["Mechanics", "Electronics", "Optics", "Laboratory Work"],
        },
        "chemistry": {
            "icon": "⚗️",
            "name": "Chemistry",
            "description": "The Chemistry Department offers quality education in organic, inorganic, physical and analytical chemistry with practical laboratory work.",
            "features": ["Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Lab Practice"],
        },
        "mathematics": {
            "icon": "📐",
            "name": "Mathematics",
            "description": "The Mathematics Department develops analytical thinking, problem solving, logic and mathematical reasoning skills.",
            "features": ["Algebra", "Calculus", "Statistics", "Logical Reasoning"],
        },
        "english": {
            "icon": "📖",
            "name": "English",
            "description": "The English Department focuses on language, literature, communication, grammar, writing and critical thinking.",
            "features": ["Literature", "Linguistics", "Communication", "Writing Skills"],
        },
        "urdu": {
            "icon": "📝",
            "name": "Urdu",
            "description": "The Urdu Department promotes Urdu language, literature, poetry, culture and creative expression.",
            "features": ["Urdu Literature", "Poetry", "Grammar", "Cultural Studies"],
        },
    }

    department = departments.get(slug)

    if not department:
        return render(request, "404.html")

    return render(request, "departments/detail.html", {
        "department": department
    })
def news_admissions(request):
    return render(request, "news/admissions.html")


def news_calendar(request):
    return render(request, "news/calendar.html")


def news_event(request):
    return render(request, "news/event.html")