from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Subscription, User
from foodgram.settings import (MAX_USERNAME_LENGTH, BANNED_USERNAMES,
                               MAX_FIRSTNAME_LASTNAME_LENGTH)
from recipes.models import Recipes


class UserShowSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(max_length=MAX_USERNAME_LENGTH,
                                     required=True)
    first_name = serializers.CharField(
        max_length=MAX_FIRSTNAME_LASTNAME_LENGTH, required=True)
    last_name = serializers.CharField(max_length=MAX_FIRSTNAME_LASTNAME_LENGTH,
                                      required=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    def get_is_subscribed(self, username):
        user = self.context["request"].user
        return (not user.is_anonymous and Subscription.objects.filter(
            user=user, following=username).exists())

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
        )


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with this email is already registered.")
        ])
    username = serializers.CharField(
        max_length=MAX_USERNAME_LENGTH,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with this username is already registered.")
        ])
    first_name = serializers.CharField(max_length=MAX_USERNAME_LENGTH,
                                       required=True)
    last_name = serializers.CharField(max_length=MAX_USERNAME_LENGTH,
                                      required=True)
    password = serializers.CharField(min_length=4,
                                     write_only=True,
                                     required=True,
                                     style={
                                         'input_type': 'password',
                                         'placeholder': 'Password'
                                     })

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password',
                  'role')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=MAX_USERNAME_LENGTH)
    email = serializers.EmailField(max_length=254)
    banned_names = BANNED_USERNAMES

    class Meta:
        model = User
        fields = (
            'email',
            'username',
        )

    def validate_username(self, data):
        if data in self.banned_names:
            raise serializers.ValidationError("Username not allowed")

        if User.objects.filter(username=data).exists():
            raise serializers.ValidationError("User already exists.")

        return data

    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise serializers.ValidationError(
                "A user with this email is already registered.")

        return data


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=MAX_USERNAME_LENGTH)
    confirmation_code = serializers.CharField(max_length=24)


class RecipeSmallSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'image', 'cooking_time')
        model = Recipes


class SubShowSerializer(UserShowSerializer):
    email = serializers.ReadOnlyField(source='following.email')
    id = serializers.ReadOnlyField(source='following.id')
    username = serializers.ReadOnlyField(source='following.username')
    first_name = serializers.ReadOnlyField(source='following.first_name')
    last_name = serializers.ReadOnlyField(source='following.last_name')
    is_subscribed = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()
    # recipes_count = serializers.SerializerMethodField(
    #    method_name='get_recipes_count')

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count',
        )

    def get_is_subscribed(self, username):
        return True

    def get_recipes(self, data):
        limit = self.context.get('request').query_params.get('recipes_limit')
        if not limit:
            limit = 3
        recipes = data.following.recipes.all()[:int(limit)]
        return RecipeSmallSerializer(recipes, many=True).data

    def get_recipes_count(self, data):
        return data.following.recipes.count()
