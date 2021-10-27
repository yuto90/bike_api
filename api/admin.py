from django.contrib import admin
from .models import UserProfile, Bike, Maker


class UserProfileAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('name', 'email', 'is_active', 'is_staff')
    # フィールドをリンク化
    list_display_links = ('name', 'email')


class MakerAdmin(admin.ModelAdmin):
    list_display = ('maker_name',)
    list_display_links = ('maker_name',)


class BikeAdmin(admin.ModelAdmin):
    list_display = ('bike_name', 'maker', 'category',
                    'displacement', 'created_datetime', 'updated_datetime')
    list_display_links = ('bike_name',)


# 管理画面に登録
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Maker, MakerAdmin)
admin.site.register(Bike, BikeAdmin)
