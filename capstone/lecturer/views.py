import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from .models import *

def initial(request):
    return render(request, "lecturer/initial.html")


def index(request):

    # Authenticated users view their inbox
    if request.user.is_authenticated:
        courses = Course.objects.filter(lecturer = request.user)
        context = {
            'courses' : courses,
        }
        return render(request, "lecturer/index.html", context)

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "lecturer/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "lecturer/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "lecturer/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name = last_name)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "lecturer/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "lecturer/register.html")
    
def course_view(request, id):
    course = Course.objects.get(pk = id)
    students = course.students.all()
    context = {
        'course': course,
        'students': students,
    }
    return render(request, "lecturer/course.html", context)

def class_schedule(request):
    if request.method == "POST":
        lecturer = request.user
        courses = request.POST['course']
        course = Course.objects.get(name  = courses)
        time = request.POST['time']
        schedule = Course_Schedule(lecturer=lecturer, course=course, time=time)
        schedule.save()
        HttpResponseRedirect(reverse("class"))

    course_schedule = Course_Schedule.objects.filter(lecturer= request.user).order_by('time')
    courses = Course.objects.filter(lecturer = request.user)
    context = {
        'schedules': course_schedule,
        'courses': courses,
    }
    return render(request, "lecturer/class.html", context)

def notice(request):
    if request.method == "POST":
        lecturer = request.user
        courses = request.POST['course']
        course = Course.objects.get(name  = courses)
        title = request.POST['title']
        body = request.POST['body']
        notice = Notice(lecturer=lecturer, course=course, title=title, body = body)
        notice.save()
        HttpResponseRedirect(reverse("class"))
    notices = Notice.objects.filter(lecturer = request.user).order_by('time')
    courses = Course.objects.filter(lecturer = request.user)
    context = {
        'notices':notices,
        'courses': courses,
    }
    return render(request, "lecturer/notice.html", context)

def edit_notice(request, id):
    if request.method == "POST":
        notice = Notice.objects.get(pk=  id)
        notice.lecturer = request.user
        notice.title = request.POST['title']
        notice.body = request.POST['body']
        notice.save()
        HttpResponseRedirect(reverse("notice_page", args=[id]))
    notice = Notice.objects.get(pk=  id)
    context = {
        'notice':notice,
    }
    return render(request, "lecturer/notice_page.html", context)