from django.shortcuts import render,get_object_or_404
from .models import task_name
from .serializers import task_serializer
from rest_framework import generics 
from .permissions import *
from rest_framework.permissions import IsAuthenticated




# Create your views here.

class CreatePollsAPiView(generics.CreateAPIView):
    queryset = task_name.objects.all()
    serializer_class = task_serializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

   

class ListPollsApiView(generics.ListAPIView):
    queryset = task_name.objects.all()
    serializer_class = task_serializer
    permission_classes = (IsAuthenticated,StaffPermissionClass)


class UpdateStatusPollsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = task_name.objects.all()
    serializer_class = task_serializer
    permission_classes = (IsAuthenticated,StaffPermissionClass)


class DeletePolsapiView(generics.DestroyAPIView):
    queryset=task_name.objects.all()
    serializer_class = task_serializer
    permission_classes = (IsAuthenticated,StaffPermissionClass)

# class ListContentView(APIView):
#     def get(self, request):
#         all_data = task_name.objects.all()
#         serializer = task_serializer(all_data, many=True)
#         return Response(serializer.data)
    
# class DetailContentView(APIView):
#     def get(self, request, *args, **kwargs):
#         content = get_object_or_404(task_name, id=kwargs['content_id'])
#         serialzier = task_serializer(content)

#         return Response(serialzier.data)
    
# class UpdateContentView(APIView):
#     def patch(self,request, *args, **kwargs):
#         content = get_object_or_404(task_name, id=kwargs['content_id'])
#         serializer = task_serializer(task_name,data= request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
# class CreateContentView(APIView):
#     def post(self, request):
#         serializer = task_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# class DeleteContentView(APIView):
#     def delete(self,request,*args,**kwargs):
#         content = get_object_or_404(task_name, id=kwargs['content_id'])
#         content.delete()
#         return Response ({'smg':'delete'})