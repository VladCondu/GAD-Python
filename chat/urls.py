from django.urls import path

from .views import index
from . import views

app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', views.room, name='room')
]
