from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),
    path('firstHtml/', views.firsthtml, name='firsthtml'),
    path('members/', views.membersList, name='membersList'),
    path('members/info/<int:id>', views.specificmember, name='specificmember'),
]
