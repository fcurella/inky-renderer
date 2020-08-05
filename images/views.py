from rest_framework import viewsets
from rest_framework.decorators import action

from . import models, serializers


class ScreenViewSet(viewsets.ViewSet):
    queryset = models.Screen.objects.all()
    serializer_class = serializers.ScreenSerializer

    @action(detail=True, methods=['post'])
    def show(self, request, pk=None):
        ...

