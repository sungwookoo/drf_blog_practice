from rest_framework import serializers

from blog.models import Article as ArticleModel
from blog.models import Category as CategoryModel
from blog.models import Comment as CommentModel


class ArticleUserSerializer(serializers.ModelSerializer):
    pass


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            "name",
            "desc",
        ]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = CommentModel
        fields = [
            "article",
            "user",
            "content",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True, read_only=True)
    category = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source="comment_set")

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = ArticleModel
        fields = [
            # "author",
            "title",
            "content",
            "category",
            "comments",
        ]

    def create(self, validated_data):
        categories = validated_data.pop('category')
        return ArticleModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
