from django.urls import path
from .views import *


urlpatterns = [
    path('all_content',ListPollsApiView.as_view()),
    path('detail/<int:content_id>',DeletePolsapiView.as_view()),
    path('update/<int:content_id>',UpdateStatusPollsView.as_view()),
    path('create/',CreatePollsAPiView.as_view()),

]