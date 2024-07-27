# Generated by Django 5.0.7 on 2024-07-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок новости')),
                ('description', models.TextField(verbose_name='Описание новости')),
                ('photo', models.ImageField(upload_to='news/', verbose_name='Фотография')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]