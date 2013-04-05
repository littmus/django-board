# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from board.models import *
from article.models import *

category_list = Category.objects.all()
board_list = Board.objects.all()

def board_view(request, board_name):

	if request.user.is_authenticated():

		#need to check that board is exist
		if Board.objects.get(name = board_name) is None:
			return HttpResponseRedirect('/')	

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
