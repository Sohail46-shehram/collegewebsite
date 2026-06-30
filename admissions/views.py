from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AdmissionApplicationForm
from .models import AdmissionApplication


from datetime import date

def admission_portal(request):

    admission_open = date.today() >= date(2026, 8, 2)

    return render(request, "admissions/index.html", {
        "admission_open": admission_open
    })


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        messages.success(request, "Registration Successful. Please Login.")
        return redirect("login")

    return render(request, "accounts/register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")
        return redirect("login")

    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    application = AdmissionApplication.objects.filter(student=request.user).first()
    return render(request, "accounts/dashboard.html", {
        "application": application
    })


def opening_soon(request):
    return render(request, "admissions/opening_soon.html")


@login_required
def adp_apply(request):
    if AdmissionApplication.objects.filter(student=request.user).exists():
        messages.warning(request, "You have already submitted your admission application.")
        return redirect("dashboard")

    if request.method == "POST":
        form = AdmissionApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user
            application.save()

            messages.success(request, "Your admission application has been submitted successfully.")
            return redirect("dashboard")
    else:
        form = AdmissionApplicationForm()

    return render(request, "admissions/adp_apply.html", {
        "form": form
    })


@login_required
def my_application(request):
    application = AdmissionApplication.objects.filter(student=request.user).first()
    return render(request, "admissions/my_application.html", {
        "application": application
    })


@login_required
def fee_voucher(request):
    application = AdmissionApplication.objects.filter(student=request.user).first()
    return render(request, "admissions/fee_voucher.html", {
        "application": application
    })


def merit_list(request):

    selected_program = request.GET.get("program")

    applications = AdmissionApplication.objects.filter(
    status="Approved",
    is_merit_published=True
).order_by(
    "program",
    "merit_position",
    "-merit_percentage"
)

    if selected_program:
        applications = applications.filter(program=selected_program)

    applications = applications.order_by(
        "program",
        "merit_position",
        "-merit_percentage"
    )

    programs = AdmissionApplication.PROGRAM_CHOICES

    return render(request, "admissions/merit_list.html", {
        "applications": applications,
        "programs": programs,
        "selected_program": selected_program,
    })