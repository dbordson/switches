from django.urls import path

from . import views

urlpatterns = [
	path('', views.splash, name='splash'),
	path('turnoff', views.turnoff, name='turnoff'),
	path('turnon', views.turnon, name='turnon'),
]