from django.shortcuts import render
from rest_framework import generics

from test_main.serializers import BlocksSerializer, MenuSerializer
from . import models
# Create your views here.
class MenuList(generics.ListAPIView):
    queryset = models.Menu.objects.all().order_by('menu_sort')
    serializer_class = MenuSerializer

class BlockList(generics.ListAPIView):
    queryset = models.Block.objects.all().order_by('block_sort')
    serializer_class = BlocksSerializer
