# Generated by Django 3.1.2 on 2020-11-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201116_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
