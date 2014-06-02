# -*- coding: utf-8 -*-

from datetime import datetime

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

def article_write(request, board_id):

    if request.user.is_authenticated():

        return render(request, 'article_write.djhtml',
                        {
                            'categories': category_list,
                            'boards': board_list,
                            'board_id': board_id,
                        })
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def article_write_ok(request, board_id):

    if request.user.is_authenticated():    
        if request.method == "POST" and request.POST.has_key('title') and request.POST.has_key('body'):
            title = request.POST['title']
            body = request.POST['body']

            board = Board.objects.get(id=board_id)
            if board is None:
                return HttpErrorResponse("error")
            
            try:
                article_pk = Article.objects.filter(board__pk=board_id).count() + 1
                article_time = datetime.now()
                article = Article(
                            user = request.user, title = title, body = body,
                            board = board, pk_in_board=article_pk,
                            created_at = article_time, modified_at = article_time
                )
                article.save()
            except Exception as e:
                print str(e)
                return HttpErrorResponse("error")

            return HttpResponseRedirect('/board/'+board_id+'/')


        else:
            return HttpErrorResponse("error")
    else:
        return HttpErrorResponse("error")


@csrf_exempt
def article_delete_ok(request, article_id):

    if request.user.is_authenticated():

        article = Article.objects.get(id = article_id)

        if article is not None and article.user == request.user or request.user.is_superuser or request.user.is_staff:
            board_id = article.board.pk
            article.change_status('D') # or simply change status... to recover

            return HttpResponseRedirect('/board/%d/' % board_id)

        else:
            return HttpErrorResponse("error")

    else:
        return HttpErrorResponse("error")


@csrf_exempt
def article_edit(request, article_id):

    if request.user.is_authenticated():

        article = Article.objects.get(id = article_id)

        if article is None or article.user != request.user:
            return HttpErrorResponse('')

        board_id = article.board.id

        article.delete() # or simply change status... to recover


        return HttpResponseRedirect('/board/'+board_id+'/')

    else:
        return HttpErrorResponse("error")


@csrf_exempt
def article_edit_ok(request, article_id):
    return None
