# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from board.models import *
from article.models import *

category_list = Category.objects.all()
board_list = Board.objects.all()

def HttpErrorResponse(error):
    return HttpResponse('<script> alert("'+ error +'"); history.go(-1); </script>')

def article_view(request, article_id):

    if request.user.is_authenticated():

        article = Article.objects.get(id = article_id)

        if article.user != request.user:
            article.hits += 1
            article.save()

        return render(request, 'article.djhtml',
                        {
                            'categories': category_list,
                            'boards': board_list,
                            'article': article,
                        })
    else:
        return HttpResponseRedirect('/')

def article_write(request, board_name):

    if request.user.is_authenticated():

        return render(request, 'article_write.djhtml',
                        {
                            'categories': category_list,
                            'boards': board_list,
                            'board_name': board_name,
                        })
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def article_write_ok(request, board_name):

    if request.user.is_authenticated():
        
        if request.method == "POST" and request.POST.has_key('title') and request.POST.has_key('body'):

            title = request.POST['title']
            body = request.POST['body']

            board = Board.objects.get(name = board_name)
            if board is None:
                return HttpErrorResponse("error")
            
            try:
                article = Article(user = request.user, title = title, body = body, board = board)
                article.save()
            except:
                return HttpErrorResponse("error")

            return HttpResponseRedirect('/board/'+board_name+'/')


        else:
            return HttpErrorResponse("error")
    else:
        return HttpErrorResponse("error")

@csrf_exempt
def article_delete_ok(request, article_id):

    if request.user.is_authenticated():

        article = Article.objects.get(id = article_id)

        if article is not None and article.user == request.user or request.user.is_superuser or request.user.is_staff:
            board_name = article.board.name

            article.delete() # or simply change status... to recover

            return HttpResponseRedirect('/board/'+board_name+'/')

        else:
            return HttpErrorResponse("error")

    else:
        return HttpErrorResponse("error")

@csrf_exempt
def article_edit(request, article_id):

    if request.user.is_authenticated():

        article = Article.objects.get(id = article_id)

        if article is None or article.user != request.user:
            return HttpResponse('<script> alert("error"); history.go(-1) </script>')

        board_name = article.board.name

        article.delete() # or simply change status... to recover


        return HttpResponseRedirect('/board/'+board_name+'/')

    else:
        return HttpErrorResponse("error")