from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from webapp.models import Photo, Comment, Like

from api_v1.serializers import PhotoSerializer, CommentSerializer, LikeSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    #
    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return []
    #     return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_permissions(self):
    #     if self.request.method in SAFE_METHODS:
    #         return []
    #     return super().get_permissions()


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
