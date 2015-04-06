from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import yimu
from django.forms.models import model_to_dict
# Create your views here.

def App(request):
    #返回网页主应用
    return render(request,'index.html')

# class MyView(APIView):
#     permission_classes=[permissions.IsAuthenticated]
#     def get(self,request):
#         data = "Get SUCCESSFULLY"
#         return data

def select_all(request):
    lin_ban=''
    res = yimu.objects.all()
    for i in res:
        lin_ban += ' '+i.lin_ban
    return lin_ban

class MyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        #返回全部金属信息
        print(request.user)
        MI=yimu.objects.all()
        data={}
        list=[]
        for row in MI:
            list.append(model_to_dict(row,exclude='geom'))
        data["message"]="加载数据成功"
        data["data"]=list
        return Response(data)