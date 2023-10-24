from rest_framework import serializers
from .models import AuthorModel,BookModel

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('__all__')


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('__all__')


    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(BookSerializers,self).create(validated_data)
