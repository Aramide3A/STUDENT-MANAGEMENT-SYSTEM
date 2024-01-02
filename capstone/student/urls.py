from django.urls import path
from . import views 


urlpatterns = [
    path("", views.index, name="index_student"),
    path("notice", views.notice, name="notice_student"),
    path("notice/<str:id>", views.notice_page, name="notice_page_student"),
]