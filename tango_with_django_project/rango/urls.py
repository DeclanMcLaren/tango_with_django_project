from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
    url(r'about/', views.about, name='about'),
    path('', views.index, name='index'),
]
