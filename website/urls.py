from django.urls import path
from . import views

app_name = 'kechgraphix'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
]