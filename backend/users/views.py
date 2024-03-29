from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from users.models import Subscription
from users.serializers import SubShowSerializer
from recipes.models import User


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    pagination_class = PageNumberPagination

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        url_path='subscribe',
        permission_classes=[permissions.IsAuthenticatedOrReadOnly],
    )
    def subscribe(self, request, id=None):
        user = get_object_or_404(User, id=id)
        follow = Subscription.objects.filter(user=request.user, following=user)
        if request.method == 'POST':
            if user == request.user:
                error = {'errors': 'Self-subscription not allowed'}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
            obj, created = Subscription.objects.get_or_create(
                user=request.user, following=user)
            if not created:
                error = {'errors': 'You are already subscribed to this user.'}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
            serializer = SubShowSerializer(obj, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if not follow.exists():
            error = {'errors': 'You were not subscribed to this user.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly],
    )
    def subscriptions(self, request):
        pages = self.paginate_queryset(
            Subscription.objects.filter(user=request.user))

        serializer = SubShowSerializer(pages,
                                       many=True,
                                       context={'request': request})

        return self.get_paginated_response(serializer.data)
