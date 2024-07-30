from django.urls import path, include
from . import views

urlpatterns = [
    path('cbv-index/', views.IndexView.as_view(), name='cbv-index'),
    # path('go-to-maktabkhooneh/<int:pk>/', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
    path("post/", views.PostList.as_view(), name="post-list"),
    path(
        "post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"
    ),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("api/v1/", include("blog.api.v1.urls")),
]
