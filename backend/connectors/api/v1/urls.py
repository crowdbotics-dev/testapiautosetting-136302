from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136302ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136302", Testconnectors136302ViewSet, basename="testconnectors136302"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
