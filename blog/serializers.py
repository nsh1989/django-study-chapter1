from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'author',
            'body',
            'publish',
            'created',
            'updated',
            'status',
        )
        model = Post