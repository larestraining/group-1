from asyncore import write
from collections import UserString
from dataclasses import field
import email
from email.policy import default
from email.policy import default
from pyexpat import model
from random import choices
from secrets import choice
from sqlite3 import Date
from django.forms import CharField
from django.forms import IntegerField
from django.shortcuts import render
from django.db import models
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User
from rest_framework import viewsets



class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length= 20)
    last_name  = serializers.CharField(max_length= 20)
    username   = serializers.CharField(max_length= 20)
    password = serializers.CharField(max_length = 20) 
    confirm_password = serializers.CharField(write_only = True,max_length = 30)
    DOB = serializers.CharField(write_only = True,max_length = 10)
    Gender = serializers.CharField(write_only = True,max_length = 20)
    email = serializers.CharField(max_length = 20)
    address = serializers.CharField(write_only = True,max_length = 50)
    city = serializers.CharField(write_only = True,max_length = 30)
    state = serializers.CharField(write_only = True,max_length = 20)
    pincode = serializers.CharField(write_only = True, max_length = 10)
    Graduation = serializers.CharField(write_only = True,max_length = 50)
    University = serializers.CharField(write_only = True,max_length = 50)
    passout_year = serializers.CharField(write_only = True,max_length = 50)
    mark_obtained = serializers.CharField(write_only = True,max_length = 50)
    
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
            if data["password"] != data["confirmpassword"]:
                raise serializers.ValidationError("password does not match.")
            return data
    

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"],
            DOB = validated_data["DOB"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            confirm_password =validated_data["confirm_password"],
            Gender = validated_data["Gender"],
            address = validated_data[" address "],
            city = validated_data["city"],
            pincode = validated_data["pincode"],
            Graduation = validated_data["Graduation"],
            University = validated_data["University"],)

        user.set_password(validated_data["password"])
        user.save()

        return User

class Userviewsset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class= UserSerializer
