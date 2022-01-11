import django
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import  authenticate
from django.contrib.auth.models import User

from hotel_app.models import Appartments

class AppartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartments
        fields =("__all__")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',"username","email","first_name","last_name")


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        # print(data)
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")



