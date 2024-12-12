from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('search/', views.search_book, name='search_book'),
]
