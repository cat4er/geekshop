from django.contrib import admin

from .models import Contact, Product, ProductCategory

# from .models import ProductAdmin

# Register your models here.
# admin.site.register(ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Contact)
