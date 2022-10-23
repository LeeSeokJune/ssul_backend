from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def select_category(request):
    if request.method == 'POST':

        return Response('select')
