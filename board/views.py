# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from board.models import *
from article.models import *

category_list = Category.objects.all()
board_list = Board.objects.all()

PAGE_RANGE = 5
ITEMS_PER_PAGE = 1

def HttpErrorResponse(error):
	return HttpResponse('<script> alert("'+ error +'"); history.go(-1); </script>')

def board_view(request, board_name, page_num = None):

	if request.user.is_authenticated():

		#board name validation
		if Board.objects.get(name = board_name) is None:
			return HttpResponseRedirect('/')	

		article_list = Article.objects.filter(board__name = board_name).order_by('-id')
		paginator = Paginator(article_list, ITEMS_PER_PAGE)

		try:
			if page_num is not None:
				page_current = paginator.page(page_num)
			else:
				page_current = paginator.page(1)

		except PageNotAnInteger:
			return HttpErrorResponse('page number is not integer')
		except EmptyPage:
			return HttpResponseRedirect('/board/%s/' % (board_name, ))


		return render(request, 'board.djhtml',
						{
							'categories': category_list,
							'boards': board_list,
							'board_name': board_name,
							'page_current': page_current,
						})
	else:
		return HttpResponseRedirect('/')
