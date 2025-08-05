from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from api.serializers import CommentSerializer, DeveloperSerializer, GameSerializer, GenreSerializer, PlatformSerializer, RatingSerializer
from games.models import Comment, Developer, Game, Genre, Platform, Rating


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        TokenHasReadWriteScope,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ["game", "created_by"]


class DeveloperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    filterset_fields = {
        "name": ["icontains"],
    }


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.select_related("developer", "genre", "platform", "rating")
    serializer_class = GameSerializer
    filterset_fields = {
        "title": ["icontains"],
        "developer": ["exact"],
        "genre": ["exact"],
        "platform": ["exact"],
        "rating": ["exact"],
        "released_at": ["range"],
        "meta_score": ["range"],
        "user_score": ["range"],
    }


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filterset_fields = {
        "name": ["icontains"],
    }
    
    
class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    filterset_fields = {
        "name": ["icontains"],
    }
    
    
class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filterset_fields = {
        "name": ["icontains"],
    }
