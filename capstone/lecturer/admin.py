from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Course_Schedule)
admin.site.register(Notice)

