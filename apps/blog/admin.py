# coding:utf-8
"""
My admin for blog.
Contain AdminArticle.
"""
from django.contrib import admin

from models import Article, Category

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):

    """
    A simple AdminModel for Article.
    """
    search_fields = ('title',)
    fields = ('content', 'title', 'category', 'tags', 'status',
              'is_top',)

    list_display = ('title', 'is_top', 'update_time')
    list_display_links = ('title', )

    ordering = ('-update_time', )
    list_per_page = 15
    save_on_top = True

    def save_model(self, request, obj, form, change):
        '''
        Save current user to the object.user.
        '''
        obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):

    """
    A simple AdminModel for Article.
    """
    search_fields = ('name',)
    list_display = ('name', 'rank', 'is_nav', 'status', 'create_time')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
