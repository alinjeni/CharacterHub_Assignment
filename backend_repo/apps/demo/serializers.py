from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'timestamp', 'user']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'user', 'comment_count', 'comments']

    def get_comments(self, obj):
        latest_comments = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(latest_comments, many=True).data

    def get_comment_count(self, obj):
        return obj.comments.count()

# Follow-up Answer:
# To fetch 3 random comments instead of latest ones, use:
# random_comments = obj.comments.order_by('?')[:3]
