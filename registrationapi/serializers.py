from django.db import models

from django.contrib.auth.models import User

from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ('id','username','email','password','first_name', 'last_name')

        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):

        password = validated_data.pop('password',None)

        user = self.Meta.model(**validated_data)

        if(password is not None):

            user.set_password(password)

            user.save()

            return user