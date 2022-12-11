import os
from djoser.serializers import UserCreateSerializer as BaseUCS, UserSerializer as BaseUS
from .settings import BASE_DIR

from school_users.models import User

class UserCreateSerializer(BaseUCS):
    # user_type = BaseUCS.
    class Meta(BaseUCS.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'middle_name',
        'last_name', 'gender', 'phone_number']

    def create(self, validated_data):
        user_d = User(**validated_data)
        path = str(BASE_DIR) + '\\media\\users\\' + user_d.username + '\\' 
        if os.path.exists(str(BASE_DIR) + '\\media'):
            if not os.path.exists(path):
                os.makedirs(path)
                print("User Directory '% s' created." % path)
        return super().create(validated_data)


class UserSerializer(BaseUS):
    class Meta(BaseUS.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'middle_name',
                    'last_name', 'gender', 'phone_number', 'user_type']


class SimpleUserSerializer(BaseUS):
    class Meta(BaseUS.Meta):
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name']
