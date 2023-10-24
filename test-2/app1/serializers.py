from rest_framework import serializers
from .models import SiyosiyNewModel,IjtimoiyNewModels
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class siyo_serializer(serializers.ModelSerializer):
    class Meta:
        model = SiyosiyNewModel
        fields = ('new_text','pub_data','user')

class ijti_serializer(serializers.ModelSerializer):
    class Meta:
        model = IjtimoiyNewModels
        fields = ('new_text','pub_data')


def create(self,validated_data):
    validated_data['user']=get_object_or_404 (User,username= self.context['request'].user.id)
    return super(siyo_serializer,self).create(validated_data)