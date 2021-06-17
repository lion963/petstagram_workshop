from django.urls import path

from pets.views import pet_all, pet_detail, pet_like, create_pet, edit_pet, delete_pet

urlpatterns=[
    path('pets', pet_all, name='pet all'),
    path('pets/details/<int:pk>', pet_detail, name='details'),
    path('pets/like/<int:pk>', pet_like),
    path('pets/create', create_pet, name='create'),
    path('pets/edit/<int:pk>', edit_pet, name='edit'),
    path('pets/delete/<int:pk>', delete_pet, name='delete')
]