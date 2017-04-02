from rest_framework import serializers
from .models import UserProfile, Board, List, Card


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'name_first', 'name_last', 'user_id')


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'title', 'description', 'users_id')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'tite', 'description', 'boards_id')


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'title', 'description', 'comment', 'priority', 'lists_id')
