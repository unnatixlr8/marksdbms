from django.urls import re_path, path, include
from . import views

urlpatterns =[
	re_path(r'^$', views.home),

]