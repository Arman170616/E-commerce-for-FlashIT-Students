from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, blank=True, null=True, related_name='products', on_delete=models.CASCADE)
    preview_des = models.TextField(max_length=500, verbose_name='short Descriptions')
    description = models.TextField(max_length=5000, verbose_name='Descriptions')
    image = models.ImageField(upload_to='product', blank=False, null=False)
    price = models.PositiveIntegerField(default=0)
    old_price = models.FloatField(default=0.0, blank=True, null=True)
    is_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)    
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
    def get_product_url(self):
        return reverse('store:product_details', kwargs={'slug': self.slug})

    

    #auto slugify when product is created
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)