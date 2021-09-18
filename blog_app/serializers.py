from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'Description', 'draft', 'publish', 'created_at', 'updated_at',)
        model = models.Post