from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,

)
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import viewsets
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from .serializers import CardSerializer, ButtonSerializer, SocialMediaSerializer
from ...models import Card, Button, SocialMedia
from .permissions import IsOwnerOrReadOnly
from .paginations import LargeResultsSetPagination


# class CardDetail():
#     pass


class CardModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = CardSerializer
    queryset = Card.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        # "category": ["exact", "in"],
        "user": ["exact", "in"],
        "status": ["exact", "in"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = LargeResultsSetPagination
    # @action(methods=["get"], detail=False)
    # def get_ok(self, request):
    #     return Response({"detail": "ok"})


class ButtonModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ButtonSerializer
    queryset = Button.objects.all()


class SocialMediaModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()
