# Generated by Django 4.2.5 on 2023-09-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_main', '0002_remove_blocks_menu_title_blocks_text_block'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blocks',
            old_name='menu_sort',
            new_name='block_sort',
        ),
        migrations.RemoveField(
            model_name='blocks',
            name='menu_link',
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_sort',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
