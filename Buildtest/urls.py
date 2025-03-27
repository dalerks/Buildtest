from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Buildtest.blog.views import BlogViewSet, CategoryListView
router = DefaultRouter(trailing_slash=False)
# Set up the router for the Blog API
router = DefaultRouter()
router.register(r'posts', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories', CategoryListView.as_view(), name='category-list'),
]