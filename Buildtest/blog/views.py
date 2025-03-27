from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoryId']  # Enable filtering by categoryId

    # Retrieve a specific blog post by ID
    def retrieve(self, request, *args, **kwargs):
        blog = self.get_object()  # Get the blog object by ID
        serializer = self.get_serializer(blog)
        return Response(serializer.data)

    # Create a new blog post
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new blog post
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update a blog post by ID
    def update(self, request, *args, **kwargs):
        blog = self.get_object()  # Get the existing blog post
        serializer = self.get_serializer(blog, data=request.data, partial=False)  # Full update
        if serializer.is_valid():
            serializer.save()  # Save the updated blog post
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a blog post by ID
    def destroy(self, request, *args, **kwargs):
        blog = self.get_object()  # Get the blog object by ID
        blog.delete()  # Delete the blog post
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Custom DELETE method to delete all blog posts
    def delete(self, request, *args, **kwargs):
        Blog.objects.all().delete()  # Delete all blog posts
        return Response({"message": "All blogs have been deleted."}, status=status.HTTP_204_NO_CONTENT)

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()  # Fetch all categories from the database
    serializer_class = CategorySerializer  # Use the CategorySerializer to return data

  