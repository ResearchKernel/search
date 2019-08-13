from django.conf.urls import url

from .views import FetchCategoryPapersView, RecentPaperView, UniversalSearch

urlpatterns = [
    url(
        r'^papers$',
        FetchCategoryPapersView.as_view(),
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
