from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('movies/<str:id>/', views.movie, name='movie'),
    path('movies/', views.movieList, name='movies'),
]
