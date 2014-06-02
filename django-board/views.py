from django.shortcuts import render
from django.views.generic import TemplateView
from board.models import *

class IndexView(TemplateView):
    template_name = 'index.djhtml'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['boards'] = Board.objects.all()

        return context
