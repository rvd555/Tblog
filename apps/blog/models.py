#coding:utf-8
"""
My models for blog.
Contain Article.
"""
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# import ugettext_lazy for location
from django.utils.translation import ugettext_lazy as _

# Constants
STATUS = {
    0: _(u'Publish'),
    1: _(u'Draft'),
    2:_(u'Delete'),
}

class Category(models.Model):
    """
    Category model to be used for categorization of content.
    Categories are high level constructs to be used for grouping and organizing content, 
    thus creating a site's table of contents.
    #
    Use Category.available_list(AVAILABLE_CATEGORYS_NUM) to get available categorys list.
    """
    name = models.CharField(max_length=40, verbose_name=_(u'Name'))
    desc = models.CharField(max_length=100, blank=True, \
                            verbose_name=_(u'Description'), help_text=_(u'Description of a category.'))

    is_nav = models.BooleanField(default=False, verbose_name=_(u'Display on the navbar.'))

    parent = models.ForeignKey('self', default=None, \
    	                        blank=True, null=True, verbose_name=_(u'Parent category.'))

    rank = models.IntegerField(default=0, verbose_name=_(u'Display order.'))
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=_(u'Status'))

    create_time = models.DateTimeField(_(u'Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(_(u'Update Time'), auto_now=True)

    def __unicode__(self):
        if self.parent:
            return '%s:%s' % (self.parent, self.name)
        else:
            return '%s' % (self.name)

    @classmethod
    def available_list(cls, num):
        """
        A simple classmethod.
        Use Category.available_list(AVAILABLE_CATEGORYS_NUM) to get available categorys list.
        """
        return cls.objects.filter(status=0)[:num]

    class Meta:
        ordering = ['rank', '-create_time']
        verbose_name_plural = verbose_name = _(u"Category")


class Article(models.Model):
    """
    A simple model.
    Use Article.get_recently_articles(RECENTLY_ARTICLES_NUM) to get recently(RECENTLY_ARTICLES_NUM) articles.
    Use Article.get_hots_articles(HOT_ARTICLES_NUM) to get hot(HOT_ARTICLES_NUM) articles.
    Use article_object.related_articles(REALITVE_ARTICLES_NUM) to get related_articles of an object.
    """
    author = models.ForeignKey(User, verbose_name=_(u"Author"))
    category = models.ForeignKey(Category, verbose_name=_(u'Category'))

    title = models.CharField(max_length=100, verbose_name=_(u'Title'))
    tags = models.CharField(max_length=100, null=True, blank=True,\
                            verbose_name=_(u'Tags'), help_text=_(u"Use the comma(',') separated"))

    content = models.TextField(verbose_name=_(u'Content'))

    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=_(u'Status'))
    view_times = models.IntegerField(default=1)

    is_top = models.BooleanField(default=False, verbose_name=_(u'Top'))

    create_time = models.DateTimeField(_(u'Create Time'), auto_now_add=True, editable=True)
    update_time = models.DateTimeField(_(u'Update Time'), auto_now=True)

    def __unicode__(self):
        return self.title
    
    def tags_list(self):
        return [tag.strip() for tag in self.tags.split(',')]
    
    @classmethod
    def get_recently_articles(cls, num):
        """
        A simple classmethod.
        Use Article.get_recently_articles(RECENTLY_ARTICLES_NUM) to get recently(RECENTLY_ARTICLES_NUM) articles.
        """
        return cls.objects.values('title', 'view_times', 'update_time', 'author')\
            .filter(status=0).order_by('-update_time')[:num]

    @classmethod
    def get_hots_articles(cls, num):
        """
        A simple classmethod.
        Use Article.get_hots_articles(HOT_ARTICLES_NUM) to get hot(HOT_ARTICLES_NUM) articles.
        """
        return cls.objects.values('title', 'view_times', 'update_time', 'author').\
                                filter(status=0).order_by('-view_times'\
                                )[:num]

    def related_articles(self, num):
        """
        A simple method.
        Use article_object.related_articles(REALITVE_ARTICLES_NUM) to get related_articles of an object.
        """
        related_articles = None
        try:
            related_articles = Post.objects.values('title', 'view_times', 'update_time', 'author').\
                filter(tags__icontains=self.tags_list()[0]).\
                exclude(id=self.id)[:num]
        except IndexError:
            pass

        if not related_articles:
            related_articles = Post.objects.values('title', 'view_times', 'update_time', 'author').\
                filter(category=self.category).\
                exclude(id=self.id)[:num]

        return related_articles


    class Meta:
        ordering = ['-is_top', '-update_time', '-create_time']
        verbose_name_plural = verbose_name = _(u"Article")