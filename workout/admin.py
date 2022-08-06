from django.contrib import admin

from workout.models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('is_published', 'title', 'updated_at')
    list_display_links = ('title',)
    list_per_page = 5
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ('title',)}
