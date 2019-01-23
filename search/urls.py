from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = "ResearchKernel : Admin"
admin.site.site_title = "ResearchKernel : Admin"


urlpatterns = [
    url('api/v1/papers/', include('papers.urls')),
]
