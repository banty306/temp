from rest_framework import serializers
from blog.config import Config
from blog.models import BlogData


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogData
        exclude = ["updated_at"]

    def to_internal_value(self, request):
        if not request.data:
            error = Config.GENERIC.BAD_REQUEST
            raise serializers.ValidationError({"status": error[0], "message": error[1]})
        if not request.data.get("title"):
            error = Config.USER.TITLE
            raise serializers.ValidationError({"status": error[0], "message": error[1]})
        if not request.data.get("author"):
            error = Config.USER.AUTHOR
            raise serializers.ValidationError({"status": error[0], "message": error[1]})
        if not request.data.get("description"):
            error = Config.USER.DESCRIPTION
            raise serializers.ValidationError({"status": error[0], "message": error[1]})
        return request.data

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "author": instance.author,
            "key": instance.key,
            "created": instance.created_at,
            "updated": instance.updated_at
        }