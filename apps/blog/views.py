from django.shortcuts import render

from base_views import Index, Detail, List


def home(request):
    """
    View for index page.
    """
    context = (Index()).get_context()
    return render(request, 'index.html', context)


def detail(request, id):
    """
    View for detail page.
    """
    context = (Detail()).get_context(id)
    return render(request, 'detail.html', context)


def category_articles(request, category_name):
    context = (List()).get_context(CATEGORY=category_name)
    context["message"] = "There are %d articles in the category %s" %\
        (len(context["articles_list"]), category_name)
    return render(request, 'index.html', context)


def tag_articles(request, tag_name):
    context = (List()).get_context(TAG=tag_name)
    context["message"] = "There are %d articles in the tag %s" %\
        (len(context["articles_list"]), tag_name)
    return render(request, 'index.html', context)
