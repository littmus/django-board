#-*- coding:utf-8 -*-

from django import forms
from django_summernote.widgets import SummernoteInplaceWidget

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fileds = ('body')
        widgets = {
            'body': SummernoteInplaceWidget(),
        }

    def __init__(self, user=None, article=None, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.user = user
        self.article = article

    def save(self, commit=True):
        self.instance.user = self.user
        self.instance.article = self.article

        return super(CommentForm, self).save(commit=commit)

