from api.views import TagViewSet, TaskViewSet
from django.urls import include, path
from rest_framework import routers, urlpatterns

router = routers.DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
