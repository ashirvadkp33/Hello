# Generated by Django 3.1.2 on 2020-11-16 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_books_book_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='book_pic',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='stock_available',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='book_title',
            new_name='title',
        ),
    ]
