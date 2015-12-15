# coding:utf-8

from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
import cgi, cgitb
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from blog.models import Page, Comment
from .form import user_form
import os


def test_form(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            return HttpResponse(form)
    else:
        form = user_form()
    return render(request, 'test_form.html', {'form': form})


def index(request):
    page_list = Page.objects.all()
    t = get_template('index.html')
    html = t.render(Context({'page_list': page_list}))
    return HttpResponse(html)


def home(request):
    t = get_template('home.html')
    html = t.render(Context())
    return HttpResponse(html)


def about(request):
    t = get_template('about.html')
    html = t.render(Context())
    return HttpResponse(html)


def contact(request):
    t = get_template('contact.html')
    html = t.render(Context())
    return HttpResponse(html)


def page1(request, num):
    try:
        offset = int(num)
        name = 'page' + str(offset) + '.html'
        t = get_template(name)
        html = t.render(Context())
    except ValueError:
        raise Http404()
    return HttpResponse(html)


@csrf_exempt
def page(request):
    page_id = request.GET['id']
    page = Page.objects.get(id=page_id)

    comment_list = Comment.objects.filter(comment_page=page)

    t = get_template('page.html')
    html = t.render(Context({'page': page, 'comment_list': comment_list}))
    return HttpResponse(html)


@csrf_exempt
def comment(request):
    comment_id = request.GET['id']
    comment = Comment.objects.get(id=comment_id)
    t = get_template('comment.html')
    html = t.render(Context({'comment': comment}))
    return HttpResponse(html)


def write_new_page(request):
    t = get_template('write.html')
    html = t.render(Context())
    return HttpResponse(html)


@csrf_exempt
def add_new_page(request):
    password = str(request.POST['password'])
    if password == 'qianyu':
        title = str(request.POST['title'])
        if title == '':
            title = "无标题"
        content = str(request.POST['content'])
        page = Page.objects.create(page_title=title, page_content=content)
        page.save()
    t = get_template('home.html')
    html = t.render(Context())
    return HttpResponse(html)


@csrf_exempt
def add_new_comment(request):
    page_id = str(request.POST['id'])
    name = str(request.POST['name'])
    if name == '':
        name = "匿名用户"
    content = str(request.POST['content'])
    page = Page.objects.get(id=page_id)
    comment = Comment.objects.create(comment_name=name, comment_content=content, comment_page=page)
    comment.save()
    return HttpResponseRedirect('/page/?id=' + str(page_id))


def delete_all_page(request):
    page_list = Page.objects.all()
    page_list.delete()
    t = get_template('home.html')
    html = t.render(Context())
    return HttpResponse(html)


def delete_all_comment(request):
    comment_list = Comment.objects.all()
    comment_list.delete()
    t = get_template('home.html')
    html = t.render(Context())
    return HttpResponse(html)


@csrf_exempt
def delete_one_page(request):
    password = str(request.POST['password'])
    if password == 'qianyu':
        page_id = str(request.POST['id'])
        page = Page.objects.get(id=page_id)
        # comment_list = Comment.objects.filter(comment_page=page)
        # comment_list.delete()
        page.delete()
    t = get_template('home.html')
    html = t.render(Context())
    return HttpResponse(html)


@csrf_exempt
def delete_one_comment(request):
    password = str(request.POST['password'])
    if password == 'qianyu':
        comment_id = str(request.POST['id'])
        comment = Comment.objects.get(id=comment_id)
        page = comment.comment_page
        page_id = page.id
        comment.delete()
        return HttpResponseRedirect('/page/?id=' + str(page_id))
    t = get_template('home.html')
    html = t.render(Context())
    return HttpResponse(html)
