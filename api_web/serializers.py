from rest_framework import serializers
from .models import *
import re


class ArticleCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ['body', 'public', 'owner']

    def validate_owner(self, owner):
        if User.objects.filter(email=owner).values('role')[0]['role'] == 'subscriber':
            raise serializers.ValidationError('You are not author!')
        return owner


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['body', 'public']


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticlePrivatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class UserRegistrSerializer(serializers.ModelSerializer):

    password = serializers.CharField()

    ROLES = (
        ('subscriber', 'subscriber'),
        ('author', 'author')
    )
    role = serializers.ChoiceField(choices=ROLES, default='subscriber', allow_blank=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'role']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            role=self.validated_data['role']
        )

        password = self.validated_data['password']
        role = self.validated_data['role']
        if len(password) < 8:
            raise serializers.ValidationError(
                {password: 'пароль должен быть не короче 8 символов'}
            )
        if not re.match(r'.*\d+[a-zA-Z]+.*|[a-zA-Z]+\d+.*', password):
            raise serializers.ValidationError(
                {password: 'пароль должен быть содержать хотя бы одну цифру и букву любого регистра'}
            )
        user.set_password(password)
        user.save()
        return user
