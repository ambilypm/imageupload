from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('sort_watches/', views.sort_watches, name='sort_watches'),
    path('sort_tshirts/', views.sort_tshirts, name='sort_tshirts'),
]

