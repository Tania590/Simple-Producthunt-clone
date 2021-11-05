from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)

admin.site.register(Product,ProductAdmin)
