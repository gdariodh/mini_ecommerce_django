from rest_framework import serializers
from users.models import User

# create new user serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # encrypt the password
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance   