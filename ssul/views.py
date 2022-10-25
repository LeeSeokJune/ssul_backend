from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SsulModel
from user.models import CustomUser
# Create your views here.


@api_view(['POST'])
def register_ssul(request):
    if request.method == 'POST':
        print('register_ssul')
        return Response('asdf')


@api_view(['POST'])
def get_ssul(request):
    if request.method == 'POST':
        print('get_ssul')
        return Response()
