"""first_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^index$',views.index),
    url(r'^about$',views.about),
    url(r'^contact$',views.contact),
    url(r'^page(\d+)$',views.page1),
    url(r'^page/$',views.page),
    url(r'^comment/$',views.comment),
    url(r'^write_new_page$',views.write_new_page),
    url(r'^add_new_page$',views.add_new_page),
    url(r'^add_new_comment$',views.add_new_comment),
    #url(r'^delete_all_page$', 'blog.views.delete_all_page', name='delete_all_page'),
    #url(r'^delete_all_comment$', 'blog.views.delete_all_comment', name='delete_all_comment'),
    url(r'^delete_one_page$',views.delete_one_page),
    url(r'^delete_one_comment$',views.delete_one_comment),
    url(r'^test_form$',views.test_form),
    url(r'^admin/', include(admin.site.urls)),
]
