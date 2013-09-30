from django.shortcuts import render

from board.models import *

def index(request):

    category_list = Category.objects.all()
    board_list = Board.objects.all()

    return render(request, 'index.djhtml',
                    {
                        'categories': category_list,
                        'boards': board_list,
                    })
