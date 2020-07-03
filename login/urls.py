from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path("validate", views.validate, name='validate'),
    path("register", views.register, name='register'),
    path("adduser", views.adduser, name='adduser')
]
