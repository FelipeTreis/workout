from django.urls import path

from workout import views

app_name = 'workout'

urlpatterns = [
    path('', views.home, name='home'),
    path('workout/<int:id>/', views.workout, name='workout'),
]
