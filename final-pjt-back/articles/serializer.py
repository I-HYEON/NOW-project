from rest_framework import serializers
from .models import Article, Comment

class ArticlesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id','title','updated_at')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','article')

class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'