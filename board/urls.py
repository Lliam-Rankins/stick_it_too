from django.urls import path

from . import views

urlpatterns = [
    path('board/<int:pk>', view=views.BoardListView.as_view(), name="board.board"),
]