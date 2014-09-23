from django.shortcuts import render
from django.http import Http404

from models import Category, Article
# Create your views here.


class Base(object):

    """
    A base class for blog base context.
    Use base_obj.get_base_context(AVAILABLE_CATEGORYS_NUM=10,
                                    HOT_ARTICLES_NUM=10,
                                    RECENTLY_ARTICLES_NUM=10
                                    )
            to get base_context.
    """

    def get_base_context(self,
                         AVAILABLE_CATEGORYS_NUM=100,
                         HOT_ARTICLES_NUM=10,
                         CATEGORY=None,
                         TAG=None,
                         NUM=100
                         ):
        base_context = {}
        try:
            base_context['available_category_list'] = Category.available_list(
                AVAILABLE_CATEGORYS_NUM)
            base_context['navbar_category_list'] = Category.navbar_list()
            base_context['hot_article_list'] = Article.get_hots_articles(
                HOT_ARTICLES_NUM)
            base_context['articles_list'] = Article.get_articles(
                CATEGORY, TAG, NUM)
            base_context['all_tags_list'] = Article.get_all_tags_list()
        except Exception, e:
            raise Http404
        return base_context


class Index(object):

    """
    A base class for blog index context.
    Use Index_obj.get_context() to get index_context.
    """

    index_context = {}

    def get_context(self):
        base_context = (Base()).get_base_context(NUM=100)
        context = base_context
        return context


class List(object):

    """
    A base class for blog index context.
    Use List_obj.get_context() to get index_context.
    """

    index_context = {}

    def get_context(self, CATEGORY=None, TAG=None):
        base_context = (Base()).get_base_context(
            NUM=100,
            CATEGORY=CATEGORY,
            TAG=TAG
            )
        context = base_context
        return context


class Detail(object):

    """
    A base class for blog detail context.
    Use Detail_obj.get_context() to get detail_context.
    """
    context = {}

    def get_context(self, id):
        base_context = (Base()).get_base_context(NUM=10)
        base_context["detail"] = Article.objects.get(id=id)
        base_context["related_articles"] = (Article.objects.get(id=id)).\
            related_articles(10)
        context = base_context
        return context
