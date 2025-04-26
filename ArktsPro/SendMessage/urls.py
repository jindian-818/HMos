from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('json/', views.json_view),
    path('register/', views.registerUi),
    path('search/', views.teacherSearch),
    path('subjectSearch/', views.subjectSearch),
    path('gradeSearch/', views.gradeSearch),
    path('bookingPage/', views.booking),
    path('iot/', views.iot),
    path('advise/', views.advise)
]
