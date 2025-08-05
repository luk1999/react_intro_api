from rest_framework import serializers

from games.models import Comment, Developer, Game, Genre, Platform, Rating


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "game",
            "comment",
            "created_by",
            "created_at",
        )


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = (
            "id",
            "name",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
        )
        
        
class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = (
            "id",
            "name",
        )
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            "id",
            "name",
        )


class GameSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer()
    genre = GenreSerializer()
    platform = PlatformSerializer()
    rating = RatingSerializer()

    class Meta:
        model = Game
        fields = (
            "id",
            "title",
            "slug",
            "developer",
            "genre",
            "platform",
            "rating",
            "released_at",
            "meta_score",
            "user_score",
        )
