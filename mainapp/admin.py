from django.contrib import admin
from .models import Product, ProductCategory
# from .models import ProductAdmin

# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Product)
# admin.site.register(ProductAdmin)



