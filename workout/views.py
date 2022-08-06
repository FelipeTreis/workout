from django.shortcuts import get_object_or_404, render

from workout.models import Workout


def home(request):
    workouts = Workout.objects.filter(
        is_published=True,
    ).order_by('-id')

    return render(
        request, 'workout/pages/home.html',
        context={'workout': workouts}
    )


def workout(request, id):
    workout = get_object_or_404(Workout, pk=id, is_published=True)

    return render(
        request, 'workout/pages/workout-view.html',
        context={
            'work': workout,
            'is_detail_page': True,
        }
    )
