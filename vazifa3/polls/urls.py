from django.urls import path
from .views import GetLaptop,CreateLaptop,GetCreateLaptop,DetailUpdateDestroy
urlpatterns = [
    path('getLaptop/',GetLaptop.as_view()),
    path('createLaptop/',CreateLaptop.as_view()),
    path('getcreateLaptop/',GetCreateLaptop.as_view()),
    path('<int:pk>/',DetailUpdateDestroy.as_view())
]