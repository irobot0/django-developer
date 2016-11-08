from django.shortcuts import render

from .models import Article


def year_archieve(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    template = 'news/year_archive.html'
    context = {
        'year': year,
        'article_list': a_list,
    }
    return render(request, template, context)
