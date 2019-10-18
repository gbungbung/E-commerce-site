from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=50)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Products(models.Model):
    title = models.CharField(max_length= 50)
    img = models.ImageField(upload_to='media/%Y/%m/%d')
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description= models.TextField()
    categorie = models.ManyToManyField(Subcategory)
    recent_accessed = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=True)

    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'pk':self.pk, 'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug= slugify(self.title)
        return super().save(*args, **kwargs)



