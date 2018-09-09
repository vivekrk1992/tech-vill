# from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from maligai.models import Vehicle
from maligai.serializers import VehicleSerializer
from rest_framework.decorators import api_view, permission_classes
# from django.contrib.auth import authenticate, logout, login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
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
    else:
        print('user fresh login')
        token = Token.objects.create(user=user)
    return Response({'token': str(token)})


@api_view(['GET'])
@permission_classes((AllowAny,))
def test(request):
    print('hai')
    return Response(status=status.HTTP_200_OK)
    # return Response({'test': 'success'})


@api_view(['GET'])
def serve_vehicles(request):
    serializer = VehicleSerializer(Vehicle.objects.all(), many=True)
    return Response(serializer.data)
