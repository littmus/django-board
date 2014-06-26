#-*- coding:utf-8 -*-

from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body')

    def __init__(self, user=None, board=None, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        if isinstance(kwargs['instance'], Article):
            self.user = kwargs['instance'].user
            self.board = kwargs['instance'].board
        else:
            self.user = user
            self.board = board

        self.fields['title'].widget.attrs={'placeholder':''}
        self.fields['body'].widget.attrs={'placeholder':''}

    def save(self, commit=True):
        self.instance.user = self.user
        self.instance.board = self.board

        return super(ArticleForm, self).save(commit=commit)

