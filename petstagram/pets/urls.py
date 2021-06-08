from django.urls import path

from pets.views import pet_all, pet_detail, pet_like

urlpatterns=[
    path('pets', pet_all),
    path('pets/details/<int:pk>', pet_detail),
    path('pets/like/<int:pk>', pet_like)
]