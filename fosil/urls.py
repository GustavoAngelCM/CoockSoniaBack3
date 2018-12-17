from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fosil', views.FosilCRUD)

urlpatterns = [
    path('', include(router.urls)),
    path('dominio/', views.DominioCL.as_view()),
    path('reino/', views.ReinoCL.as_view()),
    path('filo/', views.FiloCL.as_view()),
    path('clase/', views.ClaseCL.as_view()),
    path('orden/', views.OrdenCL.as_view()),
    path('familia/', views.FamiliaCL.as_view()),
    path('genero/', views.GeneroCL.as_view()),
]
