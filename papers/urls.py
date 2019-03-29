from django.conf.urls import url

from .views import *

urlpatterns = [
    url(
        r'^search/$',
        FetchPapersView.as_view(),
        name='search-papers',
    ),
    url(
        r'^search/recent$',
        RecentPaperView.as_view(),
        name='recent-papers',
    ),
]
