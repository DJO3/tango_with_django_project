from django.shortcuts import render
from rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'emphasized_message': 'This is italicized!'}
    return render(request, 'rango/about.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}

    try:
        cat = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = cat.name

        context_dict['category'] = cat
        pages = Page.objects.filter(category=cat)
        context_dict['pages'] = pages

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)
