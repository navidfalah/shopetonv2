from django.contrib import admin
from .models import myshop, Product, wishlist, postinfo, Product_Choice, IPAddress

admin.site.register(IPAddress)
admin.site.register(Product_Choice)
admin.site.register(postinfo)
admin.site.register(Product)
admin.site.register(wishlist)
admin.site.register(myshop)
