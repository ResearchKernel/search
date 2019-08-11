from django.conf.urls import url

from .views import FetchCateogryPapersView, RecentPaperView, UniversalSearch

urlpatterns = [
    url(
        r'^papers$',
        FetchCateogryPapersView.as_view(),
        name='get-feed-papers',
    ),
    url(
        r'^papers/recent$',
        RecentPaperView.as_view(),
        name='get-recent-papers',
    ),
    url(
        r'^search$',
        UniversalSearch.as_view(),
        name='universal-search',
    ),
    url(
        r'^search/advance$',
        UniversalSearch.as_view(),
        name='universal-search',
    ),


]
