# Generated by Django 3.1.2 on 2020-11-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
