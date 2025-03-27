
from rest_framework import serializers
from .models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    contents = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'contents', 'timestamp', 'categoryId']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']