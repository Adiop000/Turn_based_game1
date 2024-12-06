from django.urls import path
from TBG import views

urlpatterns = [
    path('', views.game_view, name='game_view'),
]
