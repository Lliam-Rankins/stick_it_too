from django.shortcuts import render
from django.views.generic import ListView
from .models import Note
from .models import Board

# Create your views here.
class BoardsListView(ListView):
    model = Board
    context_object = "board"

class BoardListView(ListView):
    model = Note
    content_object = "note"
    template_name = "board/board.html"