from rest_framework import serializers
from .models import Mobile


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = "__all__"
