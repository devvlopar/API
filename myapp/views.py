from django.shortcuts import render

from myapp.serializers import userSerializers
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class userList(APIView):
    def get(self,request):
        allusers = User.objects.all()
        serializer = userSerializers(allusers, many=True)
        return Response(serializer.data)
