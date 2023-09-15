from django.db import models

# Create your models here.


class Menu(models.Model):
    menu_title = models.CharField(max_length=100)
    menu_link = models.CharField(max_length=100)
    menu_sort = models.PositiveIntegerField()

    def __str__(self):
        return self.menu_title

class Block(models.Model):
    text_block = models.TextField(max_length=100)
    block_sort = models.PositiveIntegerField()


    def __str__(self):
        return self.text_block