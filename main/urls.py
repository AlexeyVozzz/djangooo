from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('tools', views.tools, name='instrument'),
    path('screen', views.screen, name='foto')
]
