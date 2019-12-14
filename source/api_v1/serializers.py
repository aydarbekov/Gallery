
from rest_framework import serializers

from webapp.models import Photo, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'Photo', 'author', 'created_at')


class PhotoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'description', 'image', 'creation_date', 'likes', 'author_name', 'comments')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'photo', 'like')

