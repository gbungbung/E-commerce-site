from django.contrib import admin
from .models import Products, Subcategory, Category

@admin.register(Products)
class ProductSlug(admin.ModelAdmin):
    prepopulated_fields= {'slug':('title', )}

admin.site.register(Subcategory)
admin.site.register(Category)