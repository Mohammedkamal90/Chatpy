# Generated by Django 5.0.6 on 2024-05-31 00:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_message_timestamp_alter_room_group'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
    migrations.RemoveField(
        model_name='message',
        name='room',
    ),
    migrations.AddField(
        model_name='message',
        name='group',
        field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.group'),
    ),
    migrations.AddField(
        model_name='message',
        name='user',
        field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
    ),
    migrations.AlterField(
        model_name='message',
        name='timestamp',
        field=models.DateTimeField(auto_now_add=True),
    ),
    migrations.DeleteModel(
        name='Room',
    ),
]

