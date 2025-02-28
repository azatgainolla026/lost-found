from django.contrib import admin
from .models import Category,Item,Tag,ItemTag

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(ItemTag)


