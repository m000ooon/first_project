from django.shortcuts import render
from django.views import View


class Homepage(View):
    def get(self, request):
        context = {
            'text': 'Добро пожаловать на сайт Компьютер.ру',
            'title': 'Компьютер.ру',
        }
        return render(request=request, template_name='core/mainpage.html', context=context)


class Info(View):
    def get(self, request):
        context = {
            'title': 'Информация',
        }
        return render(request=request, template_name='core/info.html', context=context)
