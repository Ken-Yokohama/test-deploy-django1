from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('author-list', views.authorList, name='author-list'),
    path('author-detail/<str:pk>', views.authorDetail, name='author-detail'),
    path('author-create', views.authorCreate, name='author-create'),
    path('author-update/<str:pk>', views.authorUpdate, name='author-update'),
    path('author-delete/<str:pk>', views.authorDelete, name='author-delete'),
]
