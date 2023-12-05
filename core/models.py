from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Customer(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    middle_name = models.CharField('Отчество', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True)
    reg_date = models.DateTimeField('Зарегистрирован', auto_now_add=True)
    description = models.TextField('О себе', max_length=255, blank=True)
    contact = models.CharField('Контакт', max_length=30)

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


class Advertisment(models.Model):
    owner = models.ForeignKey(Customer, verbose_name='Автор', related_name='ads', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=500, blank=True)
    price = models.DecimalField('Цена', max_length=10)
    is_active = models.BooleanField('Активно', default=False)
    rang = models.IntegerField('Ранг', max_length=1, default=1)
    dc = models.DateTimeField('Создан', auto_now_add=True)

    def __str__(self):
        return self.title


class Moderator(Customer):
    is_active = models.BooleanField('Активен', default=True)
    rang = models.IntegerField('Ранг', max_length=1, default=1)


class Message(models.Model):
    author = models.ForeignKey(Customer, verbose_name='Отправитель', related_name='messages', on_delete=models.CASCADE)
    addressee = models.ManyToManyField(Customer, verbose_name='Адресат', related_name='messages', on_delete=models.CASCADE)
    text = models.TextField('Текст', max_length=300, null=True, on_delete=models.CASCADE)
    dc = models.DateTimeField('Время отправки', auto_now_add=True)
