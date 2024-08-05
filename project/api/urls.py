from django.urls import path
from .views import *

urlpatterns = [
    path('stu_list/',stu_list.as_view()),
    path('stu_details/<int:pk>/',stu_details.as_view())
]
