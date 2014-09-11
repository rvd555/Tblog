from django.shortcuts import render
from django.http import Http404

from models import Category, Article
# Create your views here.

class Base(object):
	"""
	A base class for blog context.
	Use base_obj.get_base_context(AVAILABLE_CATEGORYS_NUM=10, HOT_ARTICLES_NUM=10, RECENTLY_ARTICLES_NUM=10) 
		to get base_context.
	"""
	def get_base_context(self, AVAILABLE_CATEGORYS_NUM=10, 
						HOT_ARTICLES_NUM=10, RECENTLY_ARTICLES_NUM=10):
		base_context={}
		try:
			base_context['available_category_list'] = Category.available_list(AVAILABLE_CATEGORYS_NUM)
			base_context['hot_article_list'] = Article.get_hots_articles(HOT_ARTICLES_NUM)
			base_context['recently_articles_list'] = Article.get_recently_articles(RECENTLY_ARTICLES_NUM)
		except Exception,e:
			raise Http404
		return base_context

class Index(Base):
	"""
	Use index_obj.get_index_context(AVAILABLE_CATEGORYS_NUM=10, HOT_ARTICLES_NUM=10, RECENTLY_ARTICLES_NUM=10) 
		to get index_context.
	"""
	def get_index_context(self, request, HOT_ARTICLES_NUM=20, RECENTLY_ARTICLES_NUM=20, TEMPLATE='index.html'):
		base_context=super(Index, self).get_base_context(HOT_ARTICLES_NUM=20, RECENTLY_ARTICLES_NUM=20)
		return render(request, TEMPLATE, base_context)




def home(request):
	home=Index()
	return home.get_index_context(request)