# Generated by Django 4.1.7 on 2023-02-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Письмо')),
                ('theme', models.CharField(max_length=1000, verbose_name='Тема')),
            ],
        ),
    ]
