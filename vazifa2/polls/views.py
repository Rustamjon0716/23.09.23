from django.shortcuts import render
from rest_framework.response import Response
from .serializer import AuthorSerializers,BookSerializers
from .models import AuthorModel,BookModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import *

# Create your views here.

class getAuthor(generics.ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class getBook(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    permission_classes = (IsAuthenticated,StaffPermissionClass)


class detailAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = (IsAuthenticated,AdminPermissionClass)
