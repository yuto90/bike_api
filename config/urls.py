from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 管理画面を表示
    path('admin/', admin.site.urls),
    # APIへの入り口
    path('api/', include('api.urls')),
]
