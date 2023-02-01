from django.urls import include, path
from rest_framework import routers
from fileUpload import views
router = routers.DefaultRouter()
router.register(r'files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls),)
]