from django.contrib import admin

from .models import CartTwo, CartTest, CartTestTwo, Details

# Register your models here.
admin.site.register(Details)
admin.site.register(CartTest)
admin.site.register(CartTestTwo)
admin.site.register(CartTwo)