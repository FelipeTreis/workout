from django.shortcuts import render


def home(request):
    return render(request, 'workout/pages/home.html')
