from django.urls import path
from .views import getAuthor,getBook,detailAuthor



urlpatterns = [
    path('getAuthor/',getAuthor.as_view()),
    path('getBook/',getBook.as_view()),
    path('detail/<int:pk>',detailAuthor.as_view())
]


