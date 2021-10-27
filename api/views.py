from api import serializers
from .models import Maker, Bike, UserProfile
from rest_framework import generics
from rest_framework import viewsets


# ListAPIView メソッド：GET 一覧取得
class BikeListView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = serializers.BikeSerializer

# ListAPIView メソッド：GET 一覧取得


class MakerListView(generics.ListAPIView):
    queryset = Maker.objects.all()
    serializer_class = serializers.MakerSerializer


# ModelViewSet　1つのエンドポイントでmodelに紐付いたCRUD処理を実装してくれる
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
