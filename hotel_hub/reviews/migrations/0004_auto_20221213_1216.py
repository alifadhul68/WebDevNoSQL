# Generated by Django 2.2.8 on 2022-12-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221213_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Hotel Name'),
        ),
    ]