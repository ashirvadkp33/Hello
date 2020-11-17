# Generated by Django 3.1.2 on 2020-11-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
                ('Phone', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='contacts',
        ),
    ]
