from . import views
from django.urls import path
urlpatterns = [
    path('movie/',views.viewMovies,name="viewMovies"),
    path('add/',views.addMovies,name="addMovies"),
    path('search/',views.searchMovies,name="searchMovies"),
    path('delete/',views.deleteMovies,name="deleteMovies"),
    path('delete/',views.deleteMovies,name="deleteMovies"),

]