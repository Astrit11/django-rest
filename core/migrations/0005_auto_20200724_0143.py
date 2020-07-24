# Generated by Django 3.0.8 on 2020-07-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200724_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breed',
            old_name='name',
            new_name='breed_name',
        ),
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dogs'),
        ),
    ]
