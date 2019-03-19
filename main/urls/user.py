from django.urls import path

from ..views import *

urlpatterns = [
  path('<int:user_id>/', UserIndex.as_view(), name='index'),
  path('', UserReg.as_view(), name='reg'),
]
