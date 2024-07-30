from django.urls import path, include
from . import views


urlpatterns = [

    path("api/v1/", include("cards.api.v1.urls")),
    path('<str:slug>/', views.business_card, name='business_card'),

]
