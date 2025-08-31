from rest_framework import generics
from .models import UserInfo
from .serializers import UserInfoSerializer
from django.shortcuts import render
# List all users & create a new user
class UserInfoListCreate(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

# Get single user by ID
class UserInfoDetail(generics.RetrieveAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = "id"   # use "id" field for lookup


def user_page(request):
    return render(request, "users.html")