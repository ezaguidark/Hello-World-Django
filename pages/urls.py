from django.urls import path
# from .views import homePageView # del archivo views.py se importa la funcion homePageView
from . import views # tambien se puede importar todo lo contenido en views.

urlpatterns = [
    path('', views.homePageView, name= "home")
]