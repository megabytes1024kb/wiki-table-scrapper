"""MoodyAssignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from olympicanalysis import views
urlpatterns = [
	url(r'^$', views.index_page),
	url(r'^scrape/', views.scrape_page),
	url(r'^visual/', views.visual_page),
    url(r'^admin/', admin.site.urls),
    url(r'^scrape-data/', views.scraper_call),
    url(r'^show-data/(?P<olympic>[\w-]+)', views.show_data),
    url(r'^get-table-data/(?P<olympic>[\w-]+)', views.get_table_data),
    url(r'^get-chart-data/(?P<olympic>[\w-]+)', views.get_chart_data),
]
