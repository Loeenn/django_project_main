# Generated by Django 4.1.7 on 2023-03-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_texts_checked_by_human'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='checked_by_human',
            field=models.IntegerField(default=0, verbose_name='Проверка проведена человеком'),
        ),
    ]
