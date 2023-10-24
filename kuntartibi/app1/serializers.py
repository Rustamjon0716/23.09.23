from rest_framework import serializers
from .models import task_name


class task_serializer(serializers.ModelSerializer):
    class Meta:
        model = task_name
        fields = ('task_name_text','pub_date','task_name_ptich')