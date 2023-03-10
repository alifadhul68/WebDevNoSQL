# Generated by Django 2.2.8 on 2022-12-09 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='reviews.Hotel'),
        ),
    ]
