from django.contrib import admin
from .models import Faculty, Students, Courses, Grades, RecordingToCourse

admin.site.register(Faculty)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Grades)
admin.site.register(RecordingToCourse)