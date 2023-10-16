from .models import TableBook,Menu
from rest_framework import serializers
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableBook
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['url', 'username', 'email', 'groups']
