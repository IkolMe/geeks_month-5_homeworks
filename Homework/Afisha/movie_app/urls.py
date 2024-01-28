from django.urls import path
from . import views


urlpatterns = [
    path('directors/', views.directors_list_view),
    path('directors/<int:id>/', views.directors_detail_view),
    path('movies/', views.movies_list_view),
    path('movies/<int:id>/', views.movies_detail_view),
    path('reviews/', views.reviews_list_view),
    path('reviews/<int:id>', views.reviews_detail_view),
]

