# Generated by Django 4.1.7 on 2023-03-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_remove_message_sub'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sub',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
