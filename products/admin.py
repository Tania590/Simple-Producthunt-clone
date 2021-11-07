from django.contrib import admin
from .models import Product, Vote

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Vote)
