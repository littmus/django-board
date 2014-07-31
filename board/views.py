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


class BoardView(SingleObjectMixin, ListView):
    model = Article
    template_name = 'django-board/board.djhtml'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(kwargs['board_pk'])
        self.paginate_by = self.object.paginate_by
        return super(BoardView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        context['current_board'] = self.object
        context['categories'] = Category.objects.all()
        context['boards'] = Board.objects.all()
        return context

    def get_object(self, board_pk):
        return get_object_or_404(Board.objects.select_related(), pk=board_pk)

    def get_queryset(self):
        return Article.objects.filter(board=self.object).values('id', 'pk_in_board', 'title', 'user__last_name', 'created_at', 'hits')

