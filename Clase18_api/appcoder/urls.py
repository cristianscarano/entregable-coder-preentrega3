from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("", inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]