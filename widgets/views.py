from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from .models import Widget


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = 'name', 'part_number'


class WidgetViewSet(ModelViewSet):
    serializer_class = WidgetSerializer
    queryset = Widget.objects.all()
