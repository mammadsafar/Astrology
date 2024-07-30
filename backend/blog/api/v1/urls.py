from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

app_name = "blog.api-v1"


router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
router.register("comment", views.CommentModelViewSet, basename="comment")


urlpatterns = router.urls


# urlpatterns = [
#     # path('post/', views.postList, name='post-list'),
#     # path('post/<id>/', views.postDetail, name='post-detail'),
#
#     # path('post/', views.PostList.as_view(), name='post-list'),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
#
#     path('post/', views.PostViewSet.as_view({'get': 'list'}), name='post-list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'path': 'partial_update', 'delete': 'destroy', }), name='post-detail'),
#
# ]
