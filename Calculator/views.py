
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.conf.urls import url
from django.contrib.auth.models import User

#from .models import Destination


class Calculator(APIView):
   
# Create your views here.
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        num1=request.data.get('num1',"")
        num2=request.data.get('num2',"")
        if(num1==""or num2==""):
            return HttpResponse("Entries not provided")
        res=num1-num2
        result = Destination.objects.create(num1 = num1, num2 = num2, res = res, operator = '-')
        result.save()
        return HttpResponse(res)
    def get(self,request):
        num1=int(request.data.get('num1',""))
        num2=int(request.data.get('num2',""))
        if(num1==" "or num2==" "):
            return HttpResponse("Entries not provided")
        res=num1+num2
        result = Destination.objects.create(num1 = num1, num2 = num2, res = res, operator = '+')
        result.save()
        return HttpResponse(res)
    def put(self,request):
        num1=int(request.data.get('num1',""))
        num2=int(request.data.get('num2',""))
        if(num1==" "or num2==" "):
            return HttpResponse("Entries not provided")
        res=num1*num2
        result = Destination.objects.create(num1 = num1, num2 = num2, res = res, operator = '*')
        result.save()
        return HttpResponse(res)
    def delete(self,request):
        num1=request.data.get('num1',"")
        num2=request.data.get('num2',"")
        if(num1==""or num2==""):
            return HttpResponse("Entries not provided")
        if(num2==0):
            return HttpResponse("Zero Division Error")
        res=num1/num2
        result = Destination.objects.create(num1 = num1, num2 = num2, res = res, operator = '/')
        result.save()
        return HttpResponse(res)
