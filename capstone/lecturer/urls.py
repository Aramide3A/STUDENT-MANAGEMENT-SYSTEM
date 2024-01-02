from django.urls import path
from . import views 


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('class', views.class_schedule, name='class'),
    path('notice', views.notice, name='notice'),
    path("course/<str:id>", views.course_view, name="course"),
    path("notice/<str:id>", views.edit_notice, name="notice_page"),
]