# Generated by Django 4.1.7 on 2023-03-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_modelhist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelhist',
            name='date',
            field=models.DateField(default='27-03-2023', verbose_name='Дата обучения'),
        ),
    ]
