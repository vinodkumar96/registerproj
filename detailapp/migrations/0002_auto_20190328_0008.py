# Generated by Django 2.1.7 on 2019-03-27 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detailapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='phmun',
            new_name='phnum',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='phmun',
            new_name='phnum',
        ),
    ]
