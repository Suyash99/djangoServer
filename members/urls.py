from django.urls import path
from . import views

urlpatterns = [
    path('general/', views.members, name='members'),
    path('members/', views.membersList, name='membersList'),
    path('members/info/<int:id>', views.specificmember, name='specificmember'),
]
