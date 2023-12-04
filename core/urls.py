from django.urls import path

from core.views import Homepage, Info

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('info/', Info.as_view(), name='information'),
]
