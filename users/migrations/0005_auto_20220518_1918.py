# Generated by Django 3.2.4 on 2022-05-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cars',
            field=models.ManyToManyField(to='users.Car', verbose_name='Los carros del usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='El nombre de la persona'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='El apellido de la persona'),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
