import app.views

from django.urls import path
from serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
class MyTokenObtainPairView(TokenObtainPairView):
    erializer_class=MyTokenObtainPairSerializer
urlpatterns = [
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]