from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password',)
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'full_name', 'sex', 'identity',
            'college', 'major', 'avatar',
        )
