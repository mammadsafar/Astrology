from rest_framework import serializers
# from ...models import Post, Category, Comment
from ...models import Card, Button, SocialMedia
from django.apps import apps

from accounts.models import Profile


class CardSerializer(serializers.ModelSerializer):
    # snippet = serializers.ReadOnlyField(source="get_snippet")
    # relative_url = serializers.URLField(
    #     source="get_absolute_api_url", read_only=True
    # )
    # absolute_url = serializers.SerializerMethodField(
    #     method_name="get_abs_url"
    # )
    class Meta:
        model = Card
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "title",
            "page_title",
            "slug",
            "image",
            "logo",
            "status",
            "created_date",
            "updated_date",
        ]

    # def get_abs_url(self, obj):
    #     request = self.context.get("request")
    #     return request.build_absolute_uri(obj.pk)

    # def to_representation(self, instance):
    #     request = self.context.get("request")
    #     rep = super().to_representation(instance)
    #     if request.parser_context.get("kwargs").get("pk"):
    #         rep.pop("snippet", None)
    #         rep.pop("relative_url", None)
    #         rep.pop("absolute_url", None)
    #     else:
    #         rep.pop("content", None)
    #     return rep

    # def create(self, validated_data):
    #     validated_data["author"] = Profile.objects.get(
    #         user__id=self.context.get("request").user.id
    #     )
    #     return super().create(validated_data)


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = ["id", "card", "text", "link"]


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ["id", "card", "icon", "link"]


