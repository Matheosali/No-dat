# Generated by Django 4.1.1 on 2022-10-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='curso',
            field=models.CharField(max_length=50),
        ),
    ]