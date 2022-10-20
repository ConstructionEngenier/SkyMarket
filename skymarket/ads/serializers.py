from rest_framework import serializers

from rest_framework.generics import get_object_or_404

from ads.models import Ad, Comment

from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    ad_id = serializers.IntegerField(source="ad.id", read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "author_id", "created_at", "author_first_name", "author_last_name", "ad_id"]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source="author.phone", read_only=True)
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)

    class Meta:
        model = Ad
        fields = ["id", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name", "author_id"]
