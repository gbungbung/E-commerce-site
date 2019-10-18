from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.db.models import Count
from django.utils import timezone
from .models import Products, Category, Subcategory

class Home(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['products']= Products.objects.all()
        return context

class ProductDetail(DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'product'
    queryset = Products.objects.all()

    def get_object(self):
        '''Record time of product accessed
        '''
        obj= super().get_object()
        obj.recent_accessed= timezone.now()
        obj.save()
        return obj


