# coding:utf-8
"""
My models for blog.
Contain Article.
"""
from datetime import datetime

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# import ugettext_lazy for location
from django.utils.translation import ugettext_lazy as _
# for markdown editor
from wmd import models as wmd_models
# for image in Article.thumbnail
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Constants
STATUS = {
    0: _(u'Publish'),
    1: _(u'Draft'),
    2: _(u'Delete'),
}


class Category(models.Model):

    """
    Category model to be used for categorization of content.
    Categories are high level constructs to be used for grouping and
    organizing content,thus creating a site's table of contents.
    #
    Use Category.available_list(AVAILABLE_CATEGORYS_NUM) to
    get available categorys list.
    """
    name = models.CharField(max_length=40, verbose_name=_(u'Name'))
    desc = models.CharField(max_length=100,
                            blank=True,
                            verbose_name=_(u'Description'),
                            help_text=_(u'Description of a category.')
                            )

    is_nav = models.BooleanField(
        default=False, verbose_name=_(u'Display on the navbar.'))

    parent = models.ForeignKey('self',
                               default=None,
                               blank=True,
                               null=True,
                               verbose_name=_(u'Parent category.')
                               )

    rank = models.IntegerField(default=0, verbose_name=_(u'Display order.'))
    status = models.IntegerField(
        default=0, choices=STATUS.items(), verbose_name=_(u'Status'))

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
        Use Category.available_list(AVAILABLE_CATEGORYS_NUM) to
        get available categorys list.
        """
        return cls.objects.filter(status=0)[:num]

    @classmethod
    def navbar_list(cls):
        """
        A simple classmethod.
        Use Category.navbar_list() to get navbar categorys list.
        """
        return cls.objects.filter(status=0).filter(is_nav=True)[:10]

    class Meta:
        ordering = ['rank', '-create_time']
        verbose_name_plural = verbose_name = _(u"Category")


class Article(models.Model):

    """
    A simple model.
    Use Article.get_articles(CATEGORY=None, TAG=None, NUM=100) to
        get available articles list.
    Use Article.get_recently_articles(RECENTLY_ARTICLES_NUM) to get
        recently(RECENTLY_ARTICLES_NUM) articles.
    Use Article.get_hots_articles(HOT_ARTICLES_NUM) to
        get hot(HOT_ARTICLES_NUM) articles.
    Use article_object.related_articles(REALITVE_ARTICLES_NUM) to
        get related_articles of an object.
    """
    author = models.ForeignKey(User, verbose_name=_(u"Author"))
    category = models.ForeignKey(Category, verbose_name=_(u'Category'))

    title = models.CharField(max_length=100, verbose_name=_(u'Title'))
    tags = models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            verbose_name=_(u'Tags'),
                            help_text=_(u"Use the comma(',') separated")
                            )

    summary = models.TextField(
        verbose_name=_(u'Summary'),
        validators=[MinLengthValidator(30)],
        error_messages={"min_length":
                        _("At least %(limit_value)d word,please!\
                            (it has %(show_value)d).")
                        }
    )
    content = wmd_models.MarkDownField(verbose_name=_(u'Content'))

    title_image = ProcessedImageField(upload_to='thumbnail',
                                      processors=[ResizeToFill(70, 70)],
                                      format='JPEG',
                                      options={'quality': 60}
                                      )

    status = models.IntegerField(
        default=0, choices=STATUS.items(), verbose_name=_(u'Status'))
    view_times = models.IntegerField(default=1)

    is_top = models.BooleanField(default=False, verbose_name=_(u'Top'))

    create_time = models.DateTimeField(
        _(u'Create Time'), auto_now_add=True, editable=True)
    update_time = models.DateTimeField(_(u'Update Time'), auto_now=True)

    def __unicode__(self):
        return self.title

    def tags_list(self):
        """
        Use article_object.tags_list() to split and get article_object's tags.
        """
        return [tag.strip() for tag in self.tags.split(',')]

    def related_articles(self, num):
        """
        A simple method.
        Use article_object.related_articles(REALITVE_ARTICLES_NUM) to
            get related_articles of an object.
        """
        related_articles = None
        try:
            related_articles = Article.objects.values('id', 'title', 'view_times', 'update_time', 'author').\
                filter(tags__icontains=self.tags_list()[0]).\
                exclude(id=self.id)[:num]
        except IndexError:
            pass

        if not related_articles:
            related_articles = Article.objects.values('id', 'title', 'view_times', 'update_time', 'author').\
                filter(category=self.category).\
                exclude(id=self.id)[:num]

        return related_articles

    @classmethod
    def get_articles(cls, CATEGORY=None, TAG=None, NUM=100):
        """
        A simple classmethod.
        Use Article.get_articles(CATEGORY=None, TAG=None, NUM=100) to
            get articles list.
        """
        if CATEGORY:
            article_list = cls.objects.filter(
                Q(status=0) & Q(category__name__icontains=CATEGORY))[:NUM]
            return article_list
        if TAG:
            article_list = cls.objects.filter(
                Q(status=0) & Q(tags__icontains=TAG))[:NUM]
            return article_list
        return cls.objects.filter(status=0)[:NUM]

    @classmethod
    def get_all_tags_list(cls):
        """
        A simple classmethod.
        Use Article.get_all_tags_list() to get all articles' tags list.
        """
        all_tags_list = []
        # obj_list = cls.objects.filter(status=0).order_by('-update_time')
        obj_list = Article.get_articles(NUM=1000)
        for obj in obj_list:
            all_tags_list = all_tags_list + obj.tags_list()
            # for tag in obj.tags.split(','):
            #     all_tags_list.append(tag)
        return all_tags_list

    @classmethod
    def get_recently_articles(cls, num):
        """
        A simple classmethod.
        Use Article.get_recently_articles(RECENTLY_ARTICLES_NUM) to
            get recently(RECENTLY_ARTICLES_NUM) articles.
        """
        return cls.objects.values('title', 'view_times', 'update_time', 'author')\
            .filter(status=0).order_by('-update_time')[:num]

    @classmethod
    def get_hots_articles(cls, num):
        """
        A simple classmethod.
        Use Article.get_hots_articles(HOT_ARTICLES_NUM) to
            get hot(HOT_ARTICLES_NUM) articles.
        """
        return cls.objects.values('id', 'title', 'view_times', 'update_time', 'author').\
            filter(status=0).order_by('-view_times'
                                      )[:num]

    class Meta:
        ordering = ['-is_top', '-update_time', '-create_time']
        verbose_name_plural = verbose_name = _(u"Article")
