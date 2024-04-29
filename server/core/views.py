from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

''' function based view
@api_view(['GET'])
def hello(request):
  return Response({'name': 'siddharth'})
'''
class Hello(APIView):
  
  def get(self, request):
    return Response({'name':'sid class'})