from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('urna/', views.register_vote_controller, name='register_vote'),
    path('report/', views.generate_controller_report, name='report_votes'),
]