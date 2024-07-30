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

from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from ...models import Post, Category, Comment
from .permissions import IsOwnerOrReadOnly
from .paginations import LargeResultsSetPagination

"""
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail': "item removed successfully"}, status=204)
"""

'''class PostList(APIView):
    """ getting a list of post and creating a new posts """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """ retreveing a list of posts"""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

'''

'''
class PostDetail(APIView):
    """ getting detail of the post and edit puts removing ir """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        """ retriveing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        """ editing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        """ deleting the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail': "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
'''

'''
class PostList(ListCreateAPIView):
    """ getting a list of post and creating a new posts """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit puts removing ir """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
'''


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact", "in"],
        "status": ["exact", "in"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = LargeResultsSetPagination
    # @action(methods=["get"], detail=False)
    # def get_ok(self, request):
    #     return Response({"detail": "ok"})


class CommentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
