from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from drf_app import views

router = DefaultRouter()
router.register('author', views.AuthorViewset)

urlpatterns = [
    url('', include(router.urls)),
]
