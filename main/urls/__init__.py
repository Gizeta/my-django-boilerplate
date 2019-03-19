from django.urls import include, path

urlpatterns = [
  path('user/', include(('main.urls.user', 'main'), namespace='user')),
]
