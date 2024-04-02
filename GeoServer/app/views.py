from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

def App(request):
    #返回网页主应用
    return render(request,'index.html')

class MyView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args, **kwargs):
        return Response("Get SUCCESSFULLY")