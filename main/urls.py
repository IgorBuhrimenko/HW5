
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student', views.show_student, name='student'),
    path('lector', views.show_lector, name='lector'),
    path('group', views.show_group, name='group')
]


