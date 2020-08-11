# Generated by Django 3.0.8 on 2020-08-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_auto_20200804_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='animal_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_breed',
            new_name='breed',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='animal',
            name='avatar',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='animal/'),
        ),
    ]
