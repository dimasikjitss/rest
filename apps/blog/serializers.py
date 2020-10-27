from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = ('id','created','title', 'description','url')

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','created','update','title','description', 'author','image')
        

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