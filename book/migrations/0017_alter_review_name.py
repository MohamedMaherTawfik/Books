# Generated by Django 4.2.7 on 2023-11-17 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_remove_book_slug_alter_author_biography_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]