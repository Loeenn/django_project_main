# Generated by Django 4.1.7 on 2023-05-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_texts_checked_by_human'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelhist',
            name='modeltype',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='modelhist',
            name='date',
            field=models.DateField(default='2023-05-16', verbose_name='Дата обучения'),
        ),
    ]