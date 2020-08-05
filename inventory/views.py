from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import response

import inky
from PIL import Image

from . import models, serializers


def show_inky(path, border=None):
    inkyphat = inky.InkyPHAT('yellow')
    with Image.open(path) as image:
        inkyphat.set_image(image)
        if border is not None:
            inkyphat.set_border(border)
        inkyphat.show()


class ScreenViewSet(viewsets.ModelViewSet):
    queryset = models.Screen.objects.all()
    serializer_class = serializers.ScreenSerializer

    @action(detail=True, methods=['post'])
    def show(self, request, pk=None):
        screen = models.Screen.objects.get(pk=pk)
        show_inky(screen.image.path, screen.border)
        return response.Response('OK')
