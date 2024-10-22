from django.urls import path
from . import views

urlpatterns = [
    path('carte/', views.show_map, name='show_map'),
    path('save_point/', views.save_point, name='save_point'),

]
