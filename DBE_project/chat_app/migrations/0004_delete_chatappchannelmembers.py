# Generated by Django 5.1.4 on 2025-01-24 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0003_chatappchannelmembers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatAppChannelMembers',
        ),
    ]
