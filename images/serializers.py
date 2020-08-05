from rest_framework import serializers

from . import models


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Screen
        fields = ['id', 'image']
