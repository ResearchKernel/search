from django.conf.urls import url

from .views import *

urlpatterns = [
    url(
        r'^papers/search$',
        FetchPapersView.as_view(),
        name='search-papers',
    ),
    url(
        r'^papers/recent$',
        RecentPaperView.as_view(),
        name='recent-papers',
    ),
]
