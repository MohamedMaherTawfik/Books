# Generated by Django 4.2.7 on 2023-11-12 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_publish_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='book_name',
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Book_Author', to='book.author'),
        ),
    ]