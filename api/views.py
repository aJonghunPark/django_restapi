from api.models import Tag, Task
from api.serializers import TagSerializer, TaskSerializer
from rest_framework import viewsets


# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
