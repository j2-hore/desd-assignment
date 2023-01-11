from django.urls import path
from . import views

urlpatterns = [
    path('add_film/', views.add_film),
    path('delete_film/<int:id>', views.delete_film),
    path('display_film/', views.display_film),
    path('add_club/', views.add_club),
    path('delete_club/<int:id>', views.delete_club),
    path('display_club/', views.display_club),
    path('add_screen/', views.add_screen),
    path('delete_screen/<int:id>', views.delete_screen),
    path('display_screen/', views.display_screen),
    path('add_showing/', views.add_showing),
    path('delete_showing/<int:id>', views.delete_showing),
    path('display_showing/', views.display_showing),
]