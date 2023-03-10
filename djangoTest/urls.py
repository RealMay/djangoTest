"""djangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers

from djangoTest.settings import MEDIA_ROOT
from oAuth.views import UserInfoViewSet, UserViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('info', UserInfoViewSet)
router_v1.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router_v1.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('storage/', include('fileUpload.urls')),
    # 读取媒体文件路径
    re_path(r'uploads/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    # ^uploads/(?P<path>.*)
]
