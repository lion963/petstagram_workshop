from django.urls import path

from common.views import landing_page, create_comment

urlpatterns=[
    path('', landing_page, name='landing'),
    path('comment/<int:pk>', create_comment, name='create comment')
]