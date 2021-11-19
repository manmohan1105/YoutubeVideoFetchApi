from django.urls import path

from . import views

urlpatterns = [
    path('new/',views.fetch_new_videos),
    path('', views.VideoList.as_view()),
    
    
]