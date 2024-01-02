from django.shortcuts import render
from .models import *
from lecturer.models import *
from datetime import datetime


def index(request):
    current_datetime = datetime.now()
    schedules = Course_Schedule.objects.filter(time__gte=current_datetime).order_by('time')
    context = {
        'schedules': schedules,
    }

    return render(request, "student/index.html", context)
    
def notice(request):
    student_notices = Notice.objects.all().order_by('-id')
    context={
        'notices': student_notices,
    }
    return render(request, 'student/notice.html', context )
    
def notice_page(request, id):
    student_notices = Notice.objects.get(pk=id)
    context={
        'notice': student_notices,
    }
    return render(request, 'student/notice_page.html', context )