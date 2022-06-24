# Generated by Django 4.0.5 on 2022-06-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fundraise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('image', models.FileField(blank=True, null=True, upload_to=None, verbose_name='Зображення')),
                ('description', models.TextField(verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Fundraise',
                'verbose_name_plural': 'Fundraises',
            },
        ),
    ]
