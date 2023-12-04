from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Student(models.Model):
    first_name = models.CharField('Имя', max_length=50, blank=True)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    middle_name = models.CharField('Отчество', max_length=50, blank=True)
    contact = models.CharField('Контакты', max_length=255, blank=True)
    is_active = models.BooleanField('Активен', default=True)
    dc = models.DateTimeField('Создан', auto_now_add=True,)

    def __str__(self):
        return self.get_full_name_str()

    def get_full_name_str(self):
        first_name = self.first_name
        middle_name = self.middle_name
        last_name = self.last_name

        if first_name:
            return f'{last_name} {first_name} {middle_name}'.strip()
        elif last_name:
            return last_name
        else:
            return 'Нет данных'


class Project(models.Model):
    student = models.ForeignKey(Student, verbose_name='Студент', on_delete=models.PROTECT, related_name='projects')
    url = models.URLField('URL')
    dc = models.DateTimeField('Создан', auto_now_add=True)

    def __str__(self):
        return f'Проект студента {str(self.student)}'


class Task(models.Model):
    students = models.ManyToManyField(Student, verbose_name='студент', related_name='tasks')
    projects = models.ManyToManyField(Project, verbose_name='проекты', related_name='tasks')
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    creator = models.ForeignKey(User, verbose_name='Создатель задачи', related_name='tasks', on_delete=models.SET_NULL, null=True,)
    deadline = models.DateField('Дедлайн', null=True)
    dc = models.DateTimeField('Создан', auto_now_add=True)

    def __str__(self):
        return self.title
