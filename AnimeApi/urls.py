"""AnimeAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from Posts import views as anim
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt
from Profiles import views as prof


router = routers.DefaultRouter()
router.register(r'users', prof.UserViewSet)
router.register(r'groups', prof.GroupViewSet)
router.register(r'anime', anim.AnimeViewSet, basename="anime")
router.register(r'genre', anim.GenreViewSet, basename="genre")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace="rest-framework")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
