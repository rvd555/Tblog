from django.shortcuts import render

from base_views import Index, Detail


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
