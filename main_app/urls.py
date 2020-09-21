from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('cats/', views.cats_index, name="cats_index"),
    path('cats/<int:TheseCats_id>/', views.cats_show, name="cats_show"),
    path('cats/create/', views.TheseCatsCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update', views.TheseCatsUpdate.as_view(), name='cats_update'),
]