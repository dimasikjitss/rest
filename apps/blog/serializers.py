from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = ('url','title', 'description',)

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','author','created', 'description', 'comments',)
        

class PostCreatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author','created', 'description',)


class CommentDetailSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('url','body','nickname',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('url','body','nickname',)