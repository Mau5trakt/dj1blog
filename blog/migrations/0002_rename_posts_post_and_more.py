# Generated by Django 5.0.3 on 2024-03-13 05:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.RenameIndex(
            model_name='post',
            new_name='blog_post_publish_bb7600_idx',
            old_name='blog_posts_publish_18b59a_idx',
        ),
    ]
