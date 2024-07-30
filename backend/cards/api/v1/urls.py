from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

app_name = "cards.api-v1"


router = DefaultRouter()
router.register("card", views.CardModelViewSet, basename="card")
router.register("button", views.ButtonModelViewSet, basename="button")
router.register("socialMedia", views.SocialMediaModelViewSet, basename="socialMedia")


urlpatterns = router.urls


# urlpatterns = [
#     # path('post/', views.postList, name='post-list'),
#     # path('post/<id>/', views.postDetail, name='post-detail'),
#
#     path('card/', views.CardList.as_view(), name='card-list'),
#     path('<int:pk>/', views.CardDetail.as_view(), name='card-detail'),
#
#     # path('post/', views.PostViewSet.as_view({'get': 'list'}), name='post-list'),
#     # path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'path': 'partial_update', 'delete': 'destroy', }), name='post-detail'),
#
# ]
