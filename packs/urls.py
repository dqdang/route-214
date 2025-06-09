# route_214/packs/urls.py

from django.urls import path
from . import views

app_name = 'packs' # Namespace for your app's URLs

urlpatterns = [
    path('', views.pack_list, name='pack_list'),
]
