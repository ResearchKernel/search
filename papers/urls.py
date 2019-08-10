from django.conf.urls import url

from .views import FetchCateogryPapersView, RecentPaperView

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
    )
]
