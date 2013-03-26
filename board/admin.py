from django.contrib import admin

from board.models import Category, Board, Article

admin.site.register(Category)
admin.site.register(Board)
admin.site.register(Article)