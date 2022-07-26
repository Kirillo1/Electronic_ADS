from django.contrib import admin

from advertisements.models import Advertisement, Category, Comment


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']
    list_filter = ['author']
    search_fields = ['title', 'author']
    fields = ['title', 'author', 'description', 'status', 'category', 'price', 'created_at', 'updated_at', 'images']
    readonly_fields = ['created_at', 'updated_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id']
    search_fields = ['name']
    fields = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    list_filter = ['id']
    search_fields = ['content']
    fields = ['content']


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Category)
admin.site.register(Comment)
