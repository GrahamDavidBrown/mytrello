from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import UserProfile, Board, List, Card
from .serializers import UserProfileSerializer, BoardSerializer, ListSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = UserProfile.objects.all().order_by('username')
    serializer_class = UserProfileSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Board.objects.all().order_by('title')
    serializer_class = BoardSerializer


class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = List.objects.all().order_by('title')
    serializer_class = ListSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Card.objects.all().order_by('priority')
    serializer_class = ListSerializer


def home(request):
    # profile = UserProfile.objects.get(user_id=request.user.id)
    # boards = Board.objects.filter(users_id=profile.user_id)
    # lists_iterable = []
    # cards = []
    # for board in boards:
    #     lists = List.objects.filter(boards_id=board.id)
    #     lists_iterable.append(List.objects.filter(boards_id=board.id))
    #     for each_list in lists:
    #         cards.append(Card.objects.filter(lists_id=each_list.id))
    # context = {'profile': profile, 'boards': boards, 'lists': lists_iterable, 'cards': cards}
    return render(request, "trello_app/home.html")
