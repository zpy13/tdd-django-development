# Generated by Django 3.2.7 on 2021-10-06 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_alter_item_list'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
