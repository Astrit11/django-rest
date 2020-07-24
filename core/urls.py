from django.urls import path
from core import views

urlpatterns = [
    path('breeds/', views.BreedView.as_view(), name='breeds'),
    path('dogs/', views.DogsView.as_view(), name='dogs'),
    path('<int:breed_id>/dogs/random', views.DogsView.as_view(), name='dogs_random'),

]