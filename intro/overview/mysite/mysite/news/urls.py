from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^article/([0-9]{4})/$', views.year_archieve),
    # url(r'^article/([0-9]{4})/([0-9]{2})/$', views.month_archieve),
    # url(r'^article/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]
