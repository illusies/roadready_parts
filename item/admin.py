from django.contrib import admin

from .models import Category, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_sold', 'created_by', 'created_at')
    list_filter = ('category', 'is_sold', 'created_by', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_by', 'created_at')

    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'description', 'price', 'image')
        }),
        ('Status', {
            'fields': ('is_sold',)
        }),
        ('Created by', {
            'fields': ('created_by', 'created_at')
        })
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(Category)
admin.site.register(Item)
