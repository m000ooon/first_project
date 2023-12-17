from django.contrib import admin

from core.models import Student, Project, Task


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact')


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ('student', 'url')


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('title', 'deadline')
