from rest_framework import serializers
from . import models


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ['id','menu_title','menu_link','menu_sort']

class BlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Block
        fields = ['id','text_block','block_sort']
