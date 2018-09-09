# from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes((AllowAny,))
def test(request):
    print('test function')
    return Response({'status': 'ok'})
