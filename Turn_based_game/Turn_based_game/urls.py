from django.urls import path
from TBG import views

urlpatterns = [
    path('', views.index, name='game_home'),       # Game start page
    path('play/', views.play_game, name='play_game'),  # Main game logic
    path('result/', views.result, name='game_result'), # Game result page
]
