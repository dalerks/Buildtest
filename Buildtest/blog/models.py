from django.db import models


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")

    def __str__(self):
        return self.title