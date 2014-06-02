# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from board.models import *
from article.models import *


PAGE_RANGE = 5
ITEMS_PER_PAGE = 10

def HttpErrorResponse(error):
    return HttpResponse('<script> alert("'+ error +'"); history.go(-1); </script>')

class BoardView(SingleObjectMixin, ListView):
    model = Article
    paginate_by = 1
    template_name = 'board.djhtml'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(kwargs['board_pk'])
        return super(BoardView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        context['current_board'] = self.object
        context['categories'] = Category.objects.all()
        context['boards'] = Board.objects.all()
        return context

    def get_object(self, board_pk):
        return get_object_or_404(Board, pk=board_pk)

    def get_queryset(self): 
        return Article.objects.filter(board__id=self.object.id).order_by('-pk')

