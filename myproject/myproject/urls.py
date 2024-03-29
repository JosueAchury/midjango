from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('admin/', admin.site.urls),
]
