# -*- coding: utf-8 -*-

from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from board.models import *
from article.models import *

from article.forms import *
#import utils

class ArticleObjectMixin(SingleObjectMixin):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleObjectMixin, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['boards'] = Board.objects.all()

        return context


class ArticleView(ArticleObjectMixin, ListView):
    template_name = 'django-board/article/article.djhtml'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(kwargs['article_pk'])

        if self.object.user != request.user:
            self.object.hits += 1
            self.object.save()

        return super(ArticleView, self).get(request, *args, **kwargs)

    def get_object(self, article_pk):
        return get_object_or_404(Article.objects.select_related(), pk=article_pk)

    def get_queryset(self):
        return None
   
    
class ArticleWriteView(ArticleObjectMixin, CreateView):
    object = None
    template_name = 'django-board/article/article_write.djhtml'
            
    def get(self, request, *args, **kwargs):
        board = Board.objects.select_related(None).get(pk=kwargs['board_pk'])
        form = ArticleForm(user=request.user, board=board)
        
        return self.render_to_response(
                self.get_context_data(form=form, board=board)
        )
         
    def post(self, request, *args, **kwargs):
        board = Board.objects.select_related(None).get(pk=kwargs['board_pk'])
        form = ArticleForm(user=request.user, board=board, data=request.POST)

        if form.is_valid():
            article = form.save()
            article.modified_at = article.created_at
            article.pk_in_board = Article.objects.filter(board__pk=board.pk).count()
            article.save()

            return HttpResponseRedirect(article.get_absolute_url())
        else:
            super(ArticleWriteView, self).post(request, *args, **kwargs)


class ArticleEditView(ArticleWriteView):
    model = Article

    def get(self, request, *args, **kwargs):
        article = Article.objects.select_related('board').get(pk=kwargs['article_pk'])
        form = ArticleForm(user=request.user, instance=article)

        return self.render_to_response(
            self.get_context_data(form=form, board=article.board)
        )

    def post(self, request, *args, **kwargs):
        article = Article.objects.select_related('board').get(pk=kwargs['article_pk'])
        form = ArticleForm(user=request.user, data=request.POST, instance=article)

        if form.is_valid():
            article = form.save()
            article.modified_at = datetime.now()
            article.save()

            return HttpResponseRedirect(article.get_absolute_url())
        else:
            super(ArticleWriteView, self).post(request, *args, **kwargs)


class ArticleDeleteView():
    pass

