# Generated by Django 4.2.7 on 2023-11-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_remove_book_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
