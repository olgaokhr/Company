# Generated by Django 4.0.1 on 2022-01-09 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_post_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_by',
            new_name='author',
        ),
    ]
