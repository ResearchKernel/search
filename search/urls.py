from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = "ResearchKernel : Admin"
admin.site.site_title = "ResearchKernel : Admin"


urlpatterns = [
    url('', include('papers.urls')),
]
