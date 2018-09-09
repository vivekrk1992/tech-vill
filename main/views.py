from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from main.serializers import *
import logging


@api_view(['POST', 'GET'])
@permission_classes((AllowAny,))
def login(request):
    print(request.data)
    print('login function')
    user_name = request.data['user_name']
    password = request.data['password']
    print(request.data)
    user = authenticate(username=user_name, password=password)
    print(user.id)
    print('user id = ', user.id)
    if Token.objects.filter(user_id=user.id).exists():
        print('user already logged')
        Token.objects.filter(user_id=user.id).delete()
        print('previous token deleted')
        token = Token.objects.create(user=user)
        print('token created for user')
        print(user.id)
        user_profile = UserProfile.objects.get(user_id=user.id)
        print(user_profile)
        serializer = UserProfileSerializer(user_profile).data
        print(serializer)
    else:
        print('user fresh login')
        token = Token.objects.create(user=user)
        user_profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(user_profile).data
    return Response({'token': str(token), 'user_profile': serializer})



@api_view(['GET'])
@permission_classes((AllowAny, ))
def test(request):
    print('test function')
    return Response({})
