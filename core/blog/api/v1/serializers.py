from rest_framework import serializers
from ...models import Post, Category
from django.urls import reverse
from accounts.models import Profile

# class PostSerializers(serializer.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class PostSerializers(serializers.ModelSerializer):
    get_absolute = serializers.SerializerMethodField(
        method_name="get_abs_url"
    )
    category = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Category.objects.all()
    )
    snippet = serializers.ReadOnlyField(source=f"get_snippet")

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "image",
            "title",
            "content",
            "snippet",
            "category",
            "status",
            "get_absolute",
            "published_date",
            "created_date",
        )
        read_only_fields = ["author"]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        req = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            req.pop("get_absolute")
        else:
            req.pop("content")
        req["Category"] = CategorySerializers(
            instance.category, context={"request": request}
        ).data
        return req

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
