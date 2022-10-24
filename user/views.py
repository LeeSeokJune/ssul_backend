from django.shortcuts import render
from django.contrib import auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def select_category(request):
    if request.method == 'POST':

        return Response('select')


@api_view(['POST'])
def register(request):
    return Response('register')


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user_data = request['POST']
        user_object = auth.authenticate(
            request, username=user_data['username'],
            password=user_data['password']
        )
        return Response('login')
