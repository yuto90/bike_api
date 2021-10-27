from rest_framework import serializers
from .models import Maker, Bike, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:

        # Serializersに紐付けるmodelを定義
        model = UserProfile

        # APIとして出力したいカラムを定義（タプル形式）
        fields = ('id', 'email', 'name', 'password')

        # fieldsの制限設定(定義したカラム名をkeyに取る)
        extra_kwargs = {
            'password': {

                # セキュリティの関係上パスワードは書き込むだけ。
                'write_only': True,

                # パスワード入力の際に「・・・」となるようにstyleを指定
                'style': {'input_type': 'password'}
            }
        }

    # ModelSerializerにデフォルトで実装されているメソッドをオーバーライド(パスワードのハッシュ化処理)
    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = "__all__"


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = "__all__"
        # fields = ('bike_name', 'maker', 'category',
        #          'displacement', 'created_datetime', 'updated_datetime')
