from django.urls import path, include
from .views import BikeListView, MakerListView, UserProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# ユーザーのCRUD処理用
# 「スラッシュ(/)は最後いらない」
router.register('profile', UserProfileViewSet)

urlpatterns = [
    # バイクの一覧取得用
    path('bike/', BikeListView.as_view(), name='bike'),
    # メーカーの一覧取得用
    path('maker/', MakerListView.as_view(), name='maker'),
    # router接続用
    path('', include(router.urls)),
]
