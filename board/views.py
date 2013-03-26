# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from board.models import *

def board_view(request):

	if request.user.is_authenticated():
		
		if request.method == "GET" and request.GET.has_key('name'):

			board_name = request.GET['name']
			#need to check that board is exist

			category_list = Category.objects.all()
			board_list = Board.objects.all()

			article_list = Article.objects.filter(board__name = board_name).order_by('-id')

			return render(request, 'board.djhtml',
							{
								'categories': category_list,
								'boards': board_list,
								'board_name': board_name,
								'articles': article_list,
							})
		else:
			return HttpResponseRedirect('/')	
	else:
		return HttpResponseRedirect('/')

def article_view(request):

	if request.user.is_authenticated():

		if request.method == "GET" and request.GET.has_key('a_id'):

			id = request.GET['a_id']

			article = Article.objects.get(id = id)

			category_list = Category.objects.all()
			board_list = Board.objects.all()

			return render(request, 'article.djhtml',
							{
								'categories': category_list,
								'boards': board_list,
								'article': article,
							})
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def article_write(request):

	if request.user.is_authenticated():

		if request.method == "GET" and request.GET.has_key('board'):

			board_name = request.GET['board']

			category_list = Category.objects.all()
			board_list = Board.objects.all()

			return render(request, 'article_write.djhtml',
							{
								'categories': category_list,
								'boards': board_list,
								'board_name': board_name,
							})
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

@csrf_exempt
def article_write_ok(request):

	if request.user.is_authenticated():

		if request.method == "POST" and request.POST.has_key('title') and request.POST.has_key('body') and request.POST.has_key('board'):

			title = request.POST['title']
			body = request.POST['body']

			board = Board.objects.get(name = request.POST['board'])
			if board is None:
				return HttpResponse('<script> alert("error"); history.go(-1); </script>')
				
			try:
				article = Article(user = request.user, title = title, body = body, board = board)
				article.save()
			except:
				return HttpResponse('<script> alert("error"); history.go(-1); </script>')

			return HttpResponseRedirect('/board/?name='+request.POST['board'])


		else:
			return HttpResponse('<script> alert("error"); history.go(-1); </script>')
	else:
		return HttpResponse('<script> alert("error"); history.go(-1); </script>')