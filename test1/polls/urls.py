from django.urls import path
from .views import CreatePollsAPiView, ListPollsApiView, UpdateStatusPollsView

urlpatterns = [
    path('create/', CreatePollsAPiView.as_view()),
    path('all/', ListPollsApiView.as_view()),
    path('update_status/<int:pk>/', UpdateStatusPollsView.as_view()),
]
