from rest_framework import serializers
from . import models
from .models import Tag

class BlogSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = models.Category
        fields = ('name', 'description', 'status', 'date_added', 'date_updated')
        
    
class PostSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.Post
         fields = ('category', 'title', 'author', 'blog_post', 'banner', 'status', 'date_added', 'date_updated')
         
         


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('user', 'contact', 'dob', 'address', 'avatar')
        


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'