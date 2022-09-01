from django.urls import path
from . import views

urlpatterns = [
               path('', views.indexView, name='home'),
               path('perfil_curso/', views.Perfilcurso, name='perfil_curso'),
               ]