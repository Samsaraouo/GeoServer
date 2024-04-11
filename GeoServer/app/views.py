from django.shortcuts import render,redirect
from django.urls import reverse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import yimu,xiaoban_huzhen
from django.forms.models import model_to_dict
from django.contrib.auth import logout
import json
from django.http import JsonResponse,HttpResponse
from django.core import serializers 
# Create your views here.

def App(request):
    #返回网页主应用
    return render(request,'index.html')

# class MyView(APIView):
#     permission_classes=[permissions.IsAuthenticated]
#     def get(self,request):
#         data = "Get SUCCESSFULLY"
#         return data



def Select_yimu(request):    
    data = {}
    data = serializers.serialize('geojson',yimu.objects.filter(lin_ban='0001'),geometry_field='geom',fields=('id','di_lei','lin_ban'))
    return HttpResponse(data)

def Select_xiaoban(request):
    data = {}
    data = serializers.serialize('geojson',xiaoban_huzhen.objects.filter(lin_ban='0001'),geometry_field='geom',fields=('id'))
    return HttpResponse(data)

def Select_linban(request):
    lb = request.POST['lb']
    data = serializers.serialize('geojson',yimu.objects.filter(lin_ban=lb),geometry_field='geom',fields=('id','di_lei','lin_ban'))
    return HttpResponse(data)

def logout_view(request):
    logout(request)
    data = {'code':'1'}
    return JsonResponse(data)