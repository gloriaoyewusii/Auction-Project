from rest_framework import serializers
from user.models import UserModel

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        user = UserModel(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
