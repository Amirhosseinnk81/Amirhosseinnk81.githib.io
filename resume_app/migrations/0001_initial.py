# Generated by Django 4.1.7 on 2023-03-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='project')),
            ],
        ),
    ]
