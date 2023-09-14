from django.contrib import admin
from shopping.models import Shopping_List, Shopping_List_Item

# Register your models here.
@admin.register(Shopping_List)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'uuid']

@admin.register(Shopping_List_Item)
class ShoppingListItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'list_id', 'quantity']