# Generated by Django 4.2.7 on 2023-11-12 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_rename_book_review_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Book_Author', to='book.author'),
        ),
    ]